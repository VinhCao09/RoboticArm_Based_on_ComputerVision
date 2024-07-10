#include <ESP32Servo.h>

// Khởi tạo đối tượng Servo
Servo servoX;
Servo servoY;
Servo servoZ;
Servo servoClaw;

// Các chân nối với servo
const int servoXPin = 27;
const int servoYPin = 26;
const int servoZPin = 25;
const int servoClawPin = 33;

void setup() {
  // Gắn các chân servo
  servoX.attach(servoXPin);
  servoY.attach(servoYPin);
  servoZ.attach(servoZPin);
  servoClaw.attach(servoClawPin);

  // Khởi tạo cổng serial
  Serial.begin(115200);
}

void loop() {
  static String inputString = "";    // Chuỗi để lưu dữ liệu nhận từ serial
  while (Serial.available()) {
    char inChar = (char)Serial.read();  // Đọc từng ký tự từ serial
    if (inChar == '\n') {               // Khi gặp ký tự newline, bắt đầu xử lý chuỗi
      int servoAngle[4] = {90, 90, 90, 90};  // [x, y, z, claw]
      int index = 0;
      char *ptr = strtok((char*)inputString.c_str(), ","); // Tách chuỗi bằng dấu phẩy
      while (ptr != NULL && index < 4) {
        servoAngle[index++] = atoi(ptr); // Chuyển đổi từng phần thành số nguyên
        ptr = strtok(NULL, ",");
      }
      // Đặt góc cho các servo
      servoX.write(servoAngle[0]);
      servoY.write(servoAngle[1]);
      servoZ.write(servoAngle[2]);
      servoClaw.write(servoAngle[3]);
      
      inputString = ""; // Reset chuỗi sau khi xử lý xong
    } else {
      inputString += inChar; // Thêm ký tự vào chuỗi
    }
  }
}
