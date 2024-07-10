import serial
import cv2
import mediapipe as mp
import time

# Cấu hình ban đầu
write_video = True  # Ghi video hay không
debug = False  # Chế độ gỡ lỗi
cam_source = 0  # Nguồn camera (0 cho camera mặc định trên laptop, 1 cho camera phụ)

# Khởi động kết nối với Arduino nếu không ở chế độ gỡ lỗi
if not debug:
    ser = serial.Serial('COM5', 115200)
    time.sleep(2)  # Đợi một chút để Arduino khởi động

# Cấu hình góc cho servo
x_min = 0
x_mid = 75
x_max = 150

# Sử dụng góc giữa cổ tay và ngón tay để điều khiển trục x
palm_angle_min = -50
palm_angle_mid = 20

y_min = 0
y_mid = 90
y_max = 180

# Sử dụng vị trí y của cổ tay để điều khiển trục y
wrist_y_min = 0.3
wrist_y_max = 0.9

z_min = 10
z_mid = 90
z_max = 180

# Sử dụng kích thước lòng bàn tay để điều khiển trục z
palm_size_min = 0.1
palm_size_max = 0.3

# Góc mở và đóng của càng gắp
claw_open_angle = 110
claw_close_angle = 92

# Góc ban đầu của servo [x, y, z, claw]
servo_angle = [x_mid, y_mid, z_mid, claw_open_angle]
prev_servo_angle = servo_angle  # Lưu góc servo trước đó để so sánh

fist_threshold = 7  # Ngưỡng để nhận biết nắm tay

# Khởi tạo các thành phần của Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(cam_source)  # Mở camera

# Cấu hình ghi video nếu cần
if write_video:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 60.0, (640, 480))

# Hàm giới hạn giá trị trong khoảng cho trước
clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

# Hàm ánh xạ giá trị từ khoảng này sang khoảng khác
map_range = lambda x, in_min, in_max, out_min, out_max: abs((x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min)

# Kiểm tra xem bàn tay có phải là nắm đấm hay không
def is_fist(hand_landmarks, palm_size):
    # Tính khoảng cách giữa cổ tay và từng đầu ngón tay
    distance_sum = 0
    WRIST = hand_landmarks.landmark[0]
    for i in [7, 8, 11, 12, 15, 16, 19, 20]:
        distance_sum += ((WRIST.x - hand_landmarks.landmark[i].x)**2 +
                         (WRIST.y - hand_landmarks.landmark[i].y)**2 +
                         (WRIST.z - hand_landmarks.landmark[i].z)**2)**0.5
    return distance_sum / palm_size < fist_threshold

# Hàm chuyển đổi tọa độ landmark của bàn tay thành góc servo
def landmark_to_servo_angle(hand_landmarks):
    servo_angle = [x_mid, y_mid, z_mid, claw_open_angle]
    WRIST = hand_landmarks.landmark[0]
    INDEX_FINGER_MCP = hand_landmarks.landmark[5]
    # Tính kích thước lòng bàn tay dựa trên khoảng cách giữa cổ tay và khớp ngón tay
    palm_size = ((WRIST.x - INDEX_FINGER_MCP.x)**2 + (WRIST.y - INDEX_FINGER_MCP.y)**2 + (WRIST.z - INDEX_FINGER_MCP.z)**2)**0.5

    # Kiểm tra nếu là nắm tay thì đóng càng gắp, ngược lại thì mở càng gắp
    if is_fist(hand_landmarks, palm_size):
        servo_angle[3] = claw_close_angle
    else:
        servo_angle[3] = claw_open_angle

    # Tính toán góc x
    distance = palm_size
    angle = (WRIST.x - INDEX_FINGER_MCP.x) / distance  # Tính radian giữa cổ tay và khớp ngón tay
    angle = int(angle * 180 / 3.1415926)  # Chuyển đổi radian sang độ
    angle = clamp(angle, palm_angle_min, palm_angle_mid)
    servo_angle[0] = map_range(angle, palm_angle_min, palm_angle_mid, x_max, x_min)

    # Tính toán góc y
    wrist_y = clamp(WRIST.y, wrist_y_min, wrist_y_max)
    servo_angle[1] = map_range(wrist_y, wrist_y_min, wrist_y_max, y_max, y_min)

    # Tính toán góc z
    palm_size = clamp(palm_size, palm_size_min, palm_size_max)
    servo_angle[2] = map_range(palm_size, palm_size_min, palm_size_max, z_max, z_min)

    # Chuyển đổi giá trị từ float sang int
    servo_angle = [int(i) for i in servo_angle]

    return servo_angle

# Xử lý video từ camera và sử dụng Mediapipe để nhận diện bàn tay
with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
            
            if len(results.multi_hand_landmarks) == 1:
                hand_landmarks = results.multi_hand_landmarks[0]
                servo_angle = landmark_to_servo_angle(hand_landmarks)

                if servo_angle != prev_servo_angle:
                    prev_servo_angle = servo_angle
                    if not debug:
                        angle_str = ','.join(map(str, servo_angle)) + '\n'
                        ser.write(angle_str.encode('utf-8'))

        # Hiển thị giá trị góc servo trên màn hình
        cv2.putText(image, f'Servo angles: {servo_angle}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (66, 25, 67), 2, cv2.LINE_AA)
        cv2.putText(image, f'Status: {"Fist" if servo_angle[3] == claw_close_angle else "Open"}', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (78, 0, 199), 2, cv2.LINE_AA)

        cv2.imshow('Arm Robot ESP32 Control OpenCV', image)

        if write_video:
            out.write(image)
        if cv2.waitKey(5) & 0xFF == 27:
            if write_video:
                out.release()
            break

cap.release()
if not debug:
    ser.close()
cv2.destroyAllWindows()
