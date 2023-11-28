import serial
import csv
import os

# 獲取當前腳本的目錄
script_dir = os.path.dirname(os.path.abspath(__file__))

# 將腳本目錄與文件名連接起來以獲得完整的路徑
csv_path = os.path.join(script_dir, 'current.csv')

# 開始連接
ser = serial.Serial('/dev/ttyUSB0', 9600)  

current_weight = None
current_pressure = None

def save_data_to_csv():
    if current_weight is not None and current_pressure is not None:
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['重量', '壓力'])
            writer.writerow([current_weight, current_pressure])

try:
    while True:
        line = ser.readline().decode('utf-8').strip()  # 讀取一行
        print(f"Received: {line}")  # 打印接收到的數據
        
        if line.startswith('[重量]'):
            current_weight = float(line.split(' ')[1])
            save_data_to_csv()
        elif line.startswith('[壓力]'):
            current_pressure = float(line.split(' ')[1])
            save_data_to_csv()
except KeyboardInterrupt:
    ser.close()  # 關閉連接
