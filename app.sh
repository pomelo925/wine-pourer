#!/bin/bash

## 開啟程式權限
chmod +x arduino/write.py
chmod +x monitor/app.py

## 執行程式
python3 arduino/write.py & 
sleep 1

python3 monitor/app.py  
pkill -f write.py # 結束背景運行的 write.py