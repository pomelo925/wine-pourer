#!/bin/bash

## 更新套件庫
sudo apt-get update

## 安裝必要的軟體包
# 通用
sudo apt install python-is-python3
sudo apt install python3-pip
sudo apt install raspi-config -y

# MPU6050
pip3 install serial
sudo apt-get install -y i2c-tools python3-smbus
