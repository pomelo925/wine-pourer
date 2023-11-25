import csv
import serial
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 獲取當前腳本的絕對路徑
current_script_path = os.path.dirname(os.path.abspath(__file__))
# 使用相對路徑建立 settings.csv 的路徑
settings_file_path = os.path.join(current_script_path, '../monitor/settings.csv')

class SettingsChangeHandler(FileSystemEventHandler):
    def __init__(self, serial_port):
        self.ser = serial_port

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('settings.csv'):
            self.update_settings()

    def update_settings(self):
        with open(settings_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if 'Angle-Servo-1' in row:
                    angle1 = row['AngleServo-1']
                    self.ser.write(f'[SERVO] 1,{angle1});\n'.encode())
                if 'Angle-Servo-2' in row:
                    angle2 = row['AngleServo-2']
                    self.ser.write(f'[SERVO] 2,{angle2});\n'.encode())

# 打開串行端口
ser = serial.Serial('/dev/ttyUSB0', 9600)

# 創建事件處理器
event_handler = SettingsChangeHandler(ser)
observer = Observer()
observer.schedule(event_handler, path=os.path.dirname(settings_file_path), recursive=False)

# 開始監控
observer.start()
try:
    while True:
        # 運行直到被 Ctrl+C 中斷
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
