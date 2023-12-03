#include "agent.h"

AGENT Agent;

AGENT::AGENT(){}

void AGENT::subscribe(){
  // 檢查是否有數據可讀
  if (Serial.available() > 0) {
    // 讀取一行數據
    String data = Serial.readStringUntil('\n');
    _processMessage(data);
  }
}

void AGENT::subscribe_test(){
  // 檢查是否有數據可讀
  if (Serial.available() > 0) {
    // 讀取一行數據
    String data = Serial.readStringUntil('\n');
    _processMessage(data);
  }
}

void AGENT::_processMessage(String data) {
  // 判斷數據類型
  if (data.startsWith("[SERVO]")) {
    Serial.print("[AGENT] received msgs "); Serial.println(data);
    _processServoMessage(data);
  } else if (data.startsWith("[TEMP]")) {
    _processTempMessage(data);
    Serial.print("[AGENT] received msgs "); Serial.println(data);
  } else if (data.startsWith("[WEIGHT]")) {
    _processWeightMessage(data);
    Serial.print("[AGENT] received msgs "); Serial.println(data);
  }
}

// 解析並執行 SERVO 相關的操作
void AGENT::_processServoMessage(String data) {
  data.remove(0, 7); // 去除訊息開頭的 "[SERVO]" 標籤

  // 找出分隔符號（逗號）的位置
  int commaIndex = data.indexOf(',');

  // 解析 servo_id 和 angle
  int servoId = data.substring(0, commaIndex).toInt();
  int angle = data.substring(commaIndex + 1).toInt();

  // 確認解析出的數值是否合理
  if (servoId >= 0 && angle >= 0 && angle <= 180) Motor.moveTo(servoId, angle);
  else Serial.println("Invalid servo data");

  return;
}

// 解析並執行 TEMP 相關的操作
void AGENT::_processTempMessage(String data) {
}

// 解析並執行 WEIGHT 相關的操作
void AGENT::_processWeightMessage(String data) {
}

