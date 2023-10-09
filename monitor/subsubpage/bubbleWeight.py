import tkinter as tk
import csv
from header import create_top_bar

class BubbleWeightPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        create_top_bar(self)
        
        # 返回按鈕
        button1 = tk.Button(self, text="Return", height=2, command=self.go_to_mainpage, font=("Helvetica", 20))
        button1.pack(fill=tk.X)
        
        # Title
        label_title = tk.Label(self, text="出泡重量設定", font=("Helvetica", 20))
        label_title.pack(pady=20)  # 位於return按鈕下方，置中
        
        # 使用Frame來組合滑桿和文字
        center_frame = tk.Frame(self)
        center_frame.pack(pady=20)
        
        # 滑桿設置
        self.slider_value = tk.IntVar()
        self.slider = tk.Scale(center_frame, from_=180, to=0, orient=tk.VERTICAL, 
                               variable=self.slider_value, command=self.update_value,
                               length=250, sliderlength=40, width=80)
        self.slider.set(0)  
        self.slider.grid(row=0, column=0, padx=20)  # 使用grid佈局
        
        # 警示文字
        self.alert_label = tk.Label(center_frame, text=f"出泡重量設定為{self.slider.get()}公克(g)", font=("Helvetica", 18), fg="red")
        self.alert_label.grid(row=0, column=1, padx=20)  # 使用grid佈局，且位於滑桿右側
        
        # 從CSV讀取值
        initial_value = self.read_value_from_csv("BubbleWeight")
        self.slider.set(initial_value if initial_value is not None else 0)


    def update_value(self, value):
        self.alert_label.config(text=f"出泡重量設定為{value}公克(g)")
        self.save_value_to_csv("BubbleWeight",value) # 存至 CSV 中
        
        
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
