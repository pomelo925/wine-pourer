#ifndef MOTOR_H
#define MOTOR_H

#include <ESP32Servo.h>

class MOTOR{
  public:
    MOTOR();
    void setupMotor();
    void moveTo(int motorNumber, int degree);
    void test_mode_auto();  // 自動測試
    void test_mode_manual(); // 手動測試

  private:
    Servo servo1, servo2;
};

extern MOTOR Motor;
#endif
