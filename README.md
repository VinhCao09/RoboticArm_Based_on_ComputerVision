
# 🤖Robotic Arm Based on Computer Vision. Microcontroller: ESP32

Robotic Arm Based on computer vision, we are using servo structure and control the project with computer and connect with ESP32 via Serial. It uses the MediaPipe to detect hand gestures and control Robot Arm.


![images](https://github.com/VinhCao09/RoboticArm_Based_on_ComputerVision/blob/main/images/1.jpg)
![images](https://github.com/VinhCao09/RoboticArm_Based_on_ComputerVision/blob/main/images/2.jpg)
![images](https://github.com/VinhCao09/RoboticArm_Based_on_ComputerVision/blob/main/images/3.jpg)

## Version Recommend
*Version Arduino IDE:*
`2.3.2`

*Version Board:* esp32 by Espressif Systems - `2.0.6`

*Version Library:* ESP32Servo by Kevin Harrington, Jhon K. Bennet - `1.2.1`

*Version Python:* `3.8.1` - https://www.npackd.org/p/org.python.Python64/3.8.1

*Version Pip:* `24.1.2`

(Python 3.8.1 include pip 19.2.3, you should consider upgrading pip 24.1.2)

Upgrade pip command:
```bash
python -m pip install --upgrade pip
```

## How to use

Upload the code to the Arduino

`⚠️Board version esp32 3.0 or higher may cause ledc error. I use version 2.0.6 which is quite good`

Install the required libraries
```bash
cd python
pip install -r requirements.txt
```
pyserial 3.5 (recommend)
```bash
pip install pyserial
```
opencv-python 4.10.0.84 (recommend)
```bash
pip install opencv-python
```
mediapipe 0.10.14 (recommend)
```bash
pip install mediapipe
```

## Set up webcam
change the cam_source in the code.
```bash
cam_source = "http://192.168.1.99/hi-images"
# 0 for camera, 1 for usbcam
```
Change the configuration
*Then, change the configuration in the python code.*
```bash
x_min = 0
x_mid = 75
x_max = 150

y_min = 0
y_mid = 90
y_max = 180

z_min = 10
z_mid = 90
z_max = 180

claw_open_angle = 120
claw_close_angle = 92
```
*//Như của mình là từ góc 92 đến góc 120 độ là tầm hoạt động của cánh tay.*

make sure the com port is correct.

```bash
ser = serial.Serial('COM5', 115200)
```

run the code.
```bash
python main4.py
```

*Sơ đồ trục Servo và kết nối*

✔️Please read the code to connect the servo pins.

✔️Please use 5V power for Servo (use external power, do not use power directly on the ESP32 board).

✔️Make sure that the ESP32 GND and external power source are connected together.

![images](https://github.com/VinhCao09/RoboticArm_Based_on_ComputerVision/blob/main/images/4.jpg)

## 🚀 About Me
Hello 👋I am Vinh. I'm studying HCMC University of Technology and Education

**Major:** Electronics and Telecommunication

**Skill:** 

*- Microcontroller:* ESP32/8266 - ARDUINO - PIC - Raspberry Pi - PLC Rockwell Allen Bradley

*- Programming languages:* C/C++/HTML/CSS/PHP/SQL and
related Frameworks (Bootstrap)

*- Communication Protocols:* SPI, I2C, UART, CAN

*- Data Trasmissions:* HTTP, TCP/IP, MQTT
## Authors

- [@my_fb](https://www.facebook.com/vcao.vn)
- [@my_email](contact@vinhcaodatabase.com)

## Demo

👉Click on the icon below to watch the demo video:

[![Watch the video](https://media3.giphy.com/media/A7LF3J4uMJQ4r8ApLg/giphy.gif?cid=6c09b95275l1l3krhehcppcrgllmv64r7jd6py964efin2av&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=s)](https://www.tiktok.com/@vinhcaoplay/video/7389532656867740944?lang=vi-VN)

https://www.tiktok.com/@vinhcaoplay/video/7389532656867740944?lang=vi-VN


![Logo](https://codingninja.asia/images/codeninjalogo.png)

