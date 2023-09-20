import tkinter as tk  
from header import create_top_bar 
from time import strftime

# 定義主頁面類別
class MainPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)  # 初始化 Frame
        self.controller = controller  # 設定控制器
        
        # 創建標題列
        create_top_bar(self)

        # 創建底部區域
        bottom_area = tk.Frame(self)
        bottom_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        # 在底部區域左側顯示數據區域
        data_text = """\
            啤酒溫度 (°C)：27 度
            托盤重量 (g)：350
            CO2 濃度 (g/L)：5.5
            累積出酒量 (L)：3.4"""
        
        data_area = tk.Label(bottom_area, text=data_text, anchor="w", font=("Helvetica", 20))
        data_area.pack(side=tk.LEFT, fill=tk.Y)

        # 在底部區域右側創建按鈕區域
        button_area = tk.Frame(bottom_area)
        button_area.pack(side=tk.RIGHT)
        
        # 計算按鈕寬度
        button_width = int(self.winfo_screenwidth() * 0.6 / 8)
        
        # 創建"開始注酒"按鈕
        start_button = tk.Button(button_area, text="開始注酒", height=2, font=("Helvetica", 20))
        start_button.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"停止注酒"按鈕
        stop_button = tk.Button(button_area, text="停止注酒", height=2, font=("Helvetica", 20))
        stop_button.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"設定"按鈕，點擊後轉到設定頁面
        settings_button = tk.Button(button_area, text="設定", font=("Helvetica", 20), height=2, command=lambda: self.go_to_settings())
        settings_button.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"酒品種類與介紹"按鈕，點擊後轉到介紹頁面
        info_button = tk.Button(button_area, text="酒品種類與介紹", font=("Helvetica", 20), height=2, command=lambda: self.go_to_introduction())
        info_button.pack(side=tk.TOP, fill=tk.X)

    # 更新時間的方法
    def update_time(self, label):
        label['text'] = strftime('%H:%M:%S %p')  # 設定當前時間
        label.after(1000, self.update_time, label)  # 每秒更新一次
        
    # 轉到設定頁面的方法
    def go_to_settings(self):
        from subpage.settings import SettingsPage  # 從 subpage 包中引入 SettingsPage 類別
        self.controller.show_frame(SettingsPage)  # 顯示設定頁面
        
    # 轉到介紹頁面的方法
    def go_to_introduction(self):
        from subpage.introduction import IntroductionPage  # 從 subpage 包中引入 IntroductionPage 類別
        self.controller.show_frame(IntroductionPage)  # 顯示介紹頁面
