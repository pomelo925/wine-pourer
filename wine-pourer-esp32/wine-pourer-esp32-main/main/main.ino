#include <WiFi.h>

#include "motor.h"
#include "agent.h"

const char* ssid     = "your_SSID";     // Wi-Fi 名稱
const char* password = "your_PASSWORD"; // Wi-Fi 密碼

/* 功能啟用列表 */
const bool STATE_WIFI = false;  // Wi-Fi 功能
const bool STATE_MOTOR = true;  // 馬達功能
const bool STATE_AGENT = false;  // RPI 通訊功能


void setup() {
  Serial.begin(9600);
  Serial.println("Setup");

  if (STATE_MOTOR) Motor.setupMotor();
}

void loop() {
  if (STATE_AGENT) Agent.subscribe_test();
  // Motor.test_mode_auto();
  Motor.test_mode_manual();
}