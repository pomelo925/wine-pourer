import tkinter as tk 
import tkinter as ttk 

# 引入各個子頁面的類別
from mainpage import MainPage
from subpage.settings import SettingsPage
from subpage.introduction import IntroductionPage
from subsubpage.temperature import TemperaturePage
from subsubpage.beerUpperBond import BeerUpperBondPage
from subsubpage.ceaseAngle import CeaseAnglePage
from subsubpage.alcoholAngle import AlcoholAnglePage
from subsubpage.alcoholWeight import AlcoholWeightPage
from subsubpage.bubbleAngle import BubbleAnglePage
from subsubpage.bubbleWeight import BubbleWeightPage
from subsubpage.manualServo import ManualServoPage
from subsubpage.weightDetect import WeightDetectPage
from subsubpage.carbonSettings import CarbonSettingsPage


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)  # 初始化 Tkinter 的 Tk 類
        self.geometry("1080x600")  # 設定視窗大小為 400x500
        self.title("Demo APP")  # 設定窗口標題

        # 讓第一行和第一列填充任何額外的空間
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # 初始化一個字典來存儲各個子頁面（frame）的實例
        self.frames = {}
        
        # 循環創建子頁面並儲存到 self.frames 字典中
        pages = (
            MainPage, IntroductionPage, SettingsPage, 
            BeerUpperBondPage, TemperaturePage, CeaseAnglePage, AlcoholAnglePage,
            BubbleAnglePage, BubbleWeightPage, AlcoholWeightPage, ManualServoPage,
            WeightDetectPage, CarbonSettingsPage
        )

        for F in pages:
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainPage)  # 初始顯示 MainPage
    
    # 用於切換子頁面的方法
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()  # 將選定的子頁面提升到頂層

# 程式的入口點
if __name__ == "__main__":
    app = App()  # 創建 App 類的實例
    app.mainloop()  # 啟動 Tkinter 的事件循環