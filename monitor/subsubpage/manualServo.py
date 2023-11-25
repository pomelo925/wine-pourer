import tkinter as tk
import csv
from header import create_top_bar

class ManualServoPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        create_top_bar(self)

        # Return button
        button1 = tk.Button(self, text="Return", height=2, command=self.go_to_mainpage, font=("Helvetica", 20))
        button1.pack(fill=tk.X)

        # Title
        label_title = tk.Label(self, text="伺服馬達手動設定", font=("Helvetica", 20))
        label_title.pack(pady=20)

        # Create servo controls
        self.servo_controls = {}  # Store servo sliders for later reference
        for servo_name in ["Servo-1", "Servo-2"]:
            self.servo_controls[servo_name] = self.create_servo_control(self, servo_name)

        # Initialize servo values from CSV
        self.initialize_servo_values()

    def create_servo_control(self, parent, servo_name):
        frame = tk.Frame(parent, highlightbackground="black", highlightthickness=2)

        label = tk.Label(frame, text=servo_name, font=("Helvetica", 16))
        label.pack()

        slider = tk.Scale(frame, from_=0, to=180, orient=tk.HORIZONTAL, length=500, 
                          sliderlength=30, width=35, command=lambda value, name=servo_name: self.update_value(name, value))
        slider.pack(fill=tk.X)

        btn_frame = tk.Frame(frame)
        btn_decrement = tk.Button(btn_frame, text='-', command=lambda: self.adjust_slider(slider, -1))
        btn_decrement.pack(side=tk.LEFT)
        btn_increment = tk.Button(btn_frame, text='+', command=lambda: self.adjust_slider(slider, 1))
        btn_increment.pack(side=tk.LEFT)
        btn_frame.pack()

        frame.pack(pady=10)

        return slider

    def adjust_slider(self, slider, delta):
        slider.set(slider.get() + delta)

    def update_value(self, servo_name, value):
        self.save_value_to_csv(f"Angle-{servo_name}", value)

    def initialize_servo_values(self):
        for servo_name, slider in self.servo_controls.items():
            initial_value = self.read_value_from_csv(f"Angle-{servo_name}")
            if initial_value is not None:
                slider.set(initial_value)

    def read_value_from_csv(self, setting_name):
        try:
            with open('monitor/settings.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['setting'] == setting_name:
                        return int(row['value'])
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
