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

        # 一般名字 (等待變成下方的具體實作)
        button_functions = {name: lambda name=name: self.dummy_command(name) for name in button_names}
        
        # 針對每個功能的子頁面
        button_functions["警示啤酒溫度範圍"] = self.go_to_temperature
        button_functions["啤酒出酒上限"] = self.go_to_beerUpperBond
        button_functions["停止模式角度設定"] = self.go_to_ceaseAngle
        button_functions["出酒模式角度設定"] = self.go_to_alcoholAngle
        button_functions["出酒泡模式角度設定"] = self.go_to_bubbleAngle
        button_functions["出酒重量設定"] = self.go_to_alcoholWeight
        button_functions["出泡重量設定"] = self.go_to_bubbleWeight
        
        
        # 按鈕排版
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
    
    def go_to_beerUpperBond(self):
        from subsubpage.beerUpperBond import BeerUpperBondPage
        self.controller.show_frame(BeerUpperBondPage)

    def go_to_ceaseAngle(self):
        from subsubpage.ceaseAngle import CeaseAnglePage
        self.controller.show_frame(CeaseAnglePage)

    def go_to_alcoholAngle(self):
        from subsubpage.alcoholAngle import AlcoholAnglePage
        self.controller.show_frame(AlcoholAnglePage)
        
    def go_to_bubbleAngle(self):
        from subsubpage.bubbleAngle import BubbleAnglePage
        self.controller.show_frame(BubbleAnglePage)
        
    def go_to_bubbleWeight(self):
        from subsubpage.bubbleWeight import BubbleWeightPage
        self.controller.show_frame(BubbleWeightPage)

    def go_to_alcoholWeight(self):
        from subsubpage.alcoholWeight import AlcoholWeightPage
        self.controller.show_frame(AlcoholWeightPage)



