import tkinter as tk
from header import create_top_bar

class SettingsPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        create_top_bar(self)
        self.create_buttons()

    # 創建按鈕
    def create_buttons(self):
        button1 = tk.Button(self, text="Return", height=2, command=self.go_to_mainpage, font=("Helvetica", 20))
        button1.pack(fill=tk.X)

        button_names = [
            "啤酒出酒上限", "歸零累積出酒量",
            "警示啤酒溫度範圍", "CO2壓力設定和警示",
            "伺服馬達手動設定", "出酒模式角度設定",
            "出酒泡模式角度設定", "停止模式角度設定",
            "重量偵測設定", "專用杯放置後重量歸零",
            "出酒重量設定", "出泡重量設定"
        ]

        # General mapping of button names to functions
        button_functions = {name: lambda name=name: self.dummy_command(name) for name in button_names}
        
        # Special mapping for specific buttons
        button_functions["警示啤酒溫度範圍"] = self.go_to_temperature
        
        for i in range(0, len(button_names), 2):
            frame = tk.Frame(self)
            frame.pack(fill=tk.X)
            
            button1 = tk.Button(frame, text=button_names[i], height=2, width=int(self.winfo_screenwidth() * 0.3 // 10), command=button_functions[button_names[i]], font=("Helvetica", 20))
            button1.pack(side=tk.LEFT)
            
            if i + 1 < len(button_names):
                button2 = tk.Button(frame, text=button_names[i + 1], height=2, width=int(self.winfo_screenwidth() * 0.3 // 10), command=button_functions[button_names[i + 1]], font=("Helvetica", 20))
                button2.pack(side=tk.RIGHT)


    def dummy_command(self, name):
            print(f"Button {name} clicked!")

    def go_to_mainpage(self):
        from mainpage import MainPage
        self.controller.show_frame(MainPage)

    def go_to_temperature(self):
        from subsubpage.temperature import TemperaturePage
        self.controller.show_frame(TemperaturePage)

