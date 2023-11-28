#!/bin/bash

## 開啟程式權限
chmod +x esp32/write_fromEsp32.py
chmod +x esp32/write_toEsp32.py
chmod +x monitor/app.py

## 開啟 port 權限 (有連接 ESP32 時去掉註解)
#sudo chmod 777 /dev/ttyUSB0

## 執行背景程式 (有連接 ESP32 時去掉註解)
# python3 arduino/write_fromEsp32.py & 
# sleep 1
# python3 arduino/write_toEsp32.py & 
# sleep 1

## 跑主程式
python3 monitor/app.py  
pkill -f write.py # 結束背景運行的 write.py