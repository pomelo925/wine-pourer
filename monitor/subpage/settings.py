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

        # 預設 (將替換為下方具體實作)
        button_functions = {name: lambda name=name: self.dummy_command(name) for name in button_names}
        
        # 針對每個功能的子頁面
        button_functions["啤酒出酒上限"] = self.go_to_beerUpperBond
        button_functions["歸零累積出酒量"] = self.amount_tare_popup
        button_functions["警示啤酒溫度範圍"] = self.go_to_temperature
        button_functions["CO2壓力設定和警示"] = self.go_to_carbonSettings

        button_functions["伺服馬達手動設定"] = self.go_to_manualServo
        button_functions["出酒模式角度設定"] = self.go_to_alcoholAngle
        button_functions["出酒泡模式角度設定"] = self.go_to_bubbleAngle
        button_functions["停止模式角度設定"] = self.go_to_ceaseAngle

        button_functions["重量偵測設定"] = self.go_to_weightDetect
        button_functions["專用杯放置後重量歸零"] = self.weight_tare_popup
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

    def go_to_manualServo(self):
        from subsubpage.manualServo import ManualServoPage
        self.controller.show_frame(ManualServoPage)

    def go_to_weightDetect(self):
        from subsubpage.weightDetect import WeightDetectPage
        self.controller.show_frame(WeightDetectPage)

    def go_to_carbonSettings(self):
        from subsubpage.carbonSettings import CarbonSettingsPage
        self.controller.show_frame(CarbonSettingsPage)

    def weight_tare_popup(self):
        # Create a top-level window for the pop-up
        popup = tk.Toplevel(self)
        popup.title("埔樂自動精釀生啤機軟體")
        
        # Centering the popup on the screen
        popup_width = 300
        popup_height = 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (popup_width/2))
        y_cordinate = int((screen_height/2) - (popup_height/2))
        popup.geometry(f"{popup_width}x{popup_height}+{x_cordinate}+{y_cordinate}")

        # Display message
        message = tk.Label(popup, text="秤重盤已歸零。", font=("Helvetica", 16))
        message.pack(pady=10)

        # OK button to close the pop-up
        ok_button = tk.Button(popup, text="確定", height=2, command=popup.destroy, font=("Helvetica", 16))
        ok_button.pack()

    def amount_tare_popup(self):
        # Create a top-level window for the pop-up
        popup = tk.Toplevel(self)
        popup.title("埔樂自動精釀生啤機軟體")
        
        # Centering the popup on the screen
        popup_width = 300
        popup_height = 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (popup_width/2))
        y_cordinate = int((screen_height/2) - (popup_height/2))
        popup.geometry(f"{popup_width}x{popup_height}+{x_cordinate}+{y_cordinate}")

        # Display message
        message = tk.Label(popup, text="累積出酒量已歸零。", font=("Helvetica", 16))
        message.pack(pady=10)

        # OK button to close the pop-up
        ok_button = tk.Button(popup, text="確定", height=2, command=popup.destroy, font=("Helvetica", 16))
        ok_button.pack()