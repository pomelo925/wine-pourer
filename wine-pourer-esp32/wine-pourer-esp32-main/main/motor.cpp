#include "motor.h"

#define SERVO_1_PIN 2
#define SERVO_2_PIN 4

MOTOR Motor;

MOTOR::MOTOR(){}

void MOTOR::setupMotor() {
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);

  servo1.setPeriodHertz(50); // 標準 50 hz 伺服
  servo1.attach(SERVO_1_PIN, 500, 2400);

  servo2.setPeriodHertz(50); // 標準 50 hz 伺服
  servo2.attach(SERVO_2_PIN, 500, 2400);
}

void MOTOR::moveTo(int motorNumber, int degree) {
  switch(motorNumber) {
    case 1:
      servo1.write(degree);
      break;
    case 2:
      servo2.write(degree);
      break;     
  }
}

void MOTOR::test_mode_auto(){
  moveTo(1,50); moveTo(2,0);
  delay(1500);
  moveTo(1,100); moveTo(2,50);
  delay(1000);
  moveTo(1,180);
  delay(1000);
  moveTo(2,180);
  delay(2000);
}

// 輸入： 1:20 或 2:180 來控制不同馬達之角度，角度範圍 0~180

void MOTOR::test_mode_manual(){
  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n'); // Read the input from serial
    inputString.trim(); // Remove any whitespace

    if (inputString.startsWith("1:")) {
      int angle = inputString.substring(2).toInt(); // Parse the angle for servo 1
      servo1.write(angle); // Move servo 1 to the specified angle
      Serial.println("Servo 1 moved to " + String(angle));
    } else if (inputString.startsWith("2:")) {
      int angle = inputString.substring(2).toInt(); // Parse the angle for servo 2
      servo2.write(angle); // Move servo 2 to the specified angle
      Serial.println("Servo 2 moved to " + String(angle));
    }
  }
}

