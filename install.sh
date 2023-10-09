#!/bin/bash

## 安裝所有套件包，只須運行此腳本一次

## 給予其他腳本權限
chmod +x app.sh
chmod +x ros2.sh

## 更新套件庫
sudo apt-get update

## 安裝必要的軟體包
sudo apt install python-is-python3
sudo apt install python3-pip
sudo apt install raspi-config -y
python -m pip install pyserial
sudo apt-get install -y i2c-tools python3-smbus
pip install Pillow
