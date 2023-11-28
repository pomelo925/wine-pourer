import tkinter as tk
import csv
from header import create_top_bar

class WeightDetectPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        create_top_bar(self)
    
    # 返回按鈕
        button1 = tk.Button(self, text="此頁面尚未實作", height=2, command=self.go_to_mainpage, font=("Helvetica", 20))
        button1.pack(fill=tk.X)


    def update_value(self, value):
        self.alert_label.config(text=f"停止模式角度為{value}度")
        self.save_value_to_csv("CeaseAngle",value) # 存至 CSV 中
        
    
    def read_value_from_csv(self, setting_name):
        try:
            with open('monitor/settings.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == setting_name:
                        return int(row[1])
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error reading csv: {e}")
            return None
    
    
    def save_value_to_csv(self, setting_name, value):
        settings = {}
        try:
            # 讀取所有設置
            with open('monitor/settings.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    settings[row[0]] = row[1]
            
            # 更新特定設置
            settings[setting_name] = value

            # 保存所有設置
            with open('monitor/settings.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for key, value in settings.items():
                    writer.writerow([key, value])
        except Exception as e:
            print(f"Error writing to csv: {e}")
        
    def go_to_mainpage(self):
        from subpage.settings import SettingsPage
        self.controller.show_frame(SettingsPage)