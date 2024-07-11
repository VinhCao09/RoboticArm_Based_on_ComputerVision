
# Robotic Arm Based on Computer Vision. Microcontroller: ESP32

Robotic Arm Based on computer vision, we are using servo structure and control the project with computer and connect with ESP32 via Serial. It uses the MediaPipe to detect hand gestures and control Robot Arm.


![images](https://github.com/VinhCao09/RoboticArm_Based_on_ComputerVision/blob/main/images/1.jpg)
![images](https://github.com/VinhCao09/RoboticArm_Based_on_ComputerVision/blob/main/images/2.jpg)
![images](https://github.com/VinhCao09/RoboticArm_Based_on_ComputerVision/blob/main/images/3.jpg)
## 🚀 About Me
Hello 👋I am Vinh. I'm studying HCMC University of Technology and Education

**Major:** Electronics and Telecommunication

**Skill:** 

*- Microcontroller:* ESP32/8266 - ARDUINO - PIC - Raspberry Pi - PLC Rockwell Allen Bradley

*- Programming languages:* C/C++/HTML/CSS/PHP/SQL and
related Frameworks (Bootstrap)

*- Communication Protocols:* SPI, I2C, UART, CAN

*- Data Trasmissions:* HTTP, TCP/IP, MQTT


## How to use

Upload the code to the Arduino


```bash
  
```
Install the required libraries
```bash
cd python
pip install -r requirements.txt
```

Set up webcam
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

*Sơ đồ trục Servo*

![images](https://github.com/VinhCao09/RoboticArm_Based_on_ComputerVision/blob/main/images/4.jpg)

## Authors

- [@my_fb](https://www.facebook.com/vcao.vn)
- [@my_email](contact@vinhcaodatabase.com)


## Demo

https://www.tiktok.com/@vinhcaoplay/video/7389532656867740944?lang=vi-VN


![Logo](https://codingninja.asia/images/codeninjalogo.png)

