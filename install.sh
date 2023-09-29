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
pip3 install serial
sudo apt-get install -y i2c-tools python3-smbus

## 安裝 ROS2
sudo apt update
sudo apt upgrade
sudo apt install curl -y
sudo apt upgrade
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade
sudo apt install ros-humble-desktop
sudo apt install ros-dev-tools

sudo rosdep init
rosdep update

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

sudo apt autoremove

## ROS2 環境配置
source ./ros2.sh
