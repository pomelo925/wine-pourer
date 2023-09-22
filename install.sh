#!/bin/bash

## 安裝所有套件包，只須運行此腳本一次

## 更新套件庫
sudo apt-get update

## 安裝必要的軟體包
sudo apt install python-is-python3
sudo apt install python3-pip
sudo apt install raspi-config -y
pip3 install serial
sudo apt-get install -y i2c-tools python3-smbus

## 給予其他腳本權限
chmod +x app.sh
