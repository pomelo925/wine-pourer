import serial
import csv
import os

# 獲取當前腳本的目錄
script_dir = os.path.dirname(os.path.abspath(__file__))

# 將腳本目錄與文件名連接起來以獲得完整的路徑
csv_path = os.path.join(script_dir, 'current.csv')

# 開始連接
ser = serial.Serial('/dev/ttyUSB0', 9600)  # 請根據您的系統配置更新此路徑

def save_weight_to_csv(weight):
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['重量'])
        writer.writerow([weight])

try:
    while True:
        line = ser.readline().decode('utf-8').strip()  # 讀取一行
        if line.startswith('[重量]'):
            weight = float(line.split(' ')[1])
            save_weight_to_csv(weight)
except KeyboardInterrupt:
    ser.close()  # 關閉連接
