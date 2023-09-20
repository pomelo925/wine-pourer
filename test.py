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
        
        # 創建左大區
        left_big_area = tk.Frame(bottom_area)
        left_big_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 左大區的數據區
        data_text_left = """\
            啤酒溫度 (°C)：27 度
            托盤重量 (g)：350
            CO2 濃度 (g/L)：5.5
            累積出酒量 (L)：3.4"""
        data_area_left = tk.Label(left_big_area, text=data_text_left, anchor="w", font=("Helvetica", 20))
        data_area_left.pack(side=tk.LEFT, fill=tk.Y)
        
        # 左大區的按鈕區
        # 創建"開始注酒"按鈕
        start_button_left = tk.Button(left_big_area, text="開始注酒", height=2, font=("Helvetica", 20))
        start_button_left.pack(side=tk.RIGHT, fill=tk.X)
        
        # 創建"停止注酒"按鈕
        stop_button_left = tk.Button(left_big_area, text="停止注酒", height=2, font=("Helvetica", 20))
        stop_button_left.pack(side=tk.RIGHT, fill=tk.X)
        
        # 創建"設定"按鈕，點擊後轉到設定頁面
        settings_button_left = tk.Button(left_big_area, text="設定", font=("Helvetica", 20), height=2, command=lambda: self.go_to_settings())
        settings_button_left.pack(side=tk.RIGHT, fill=tk.X)
        
        # 創建"酒品種類與介紹"按鈕，點擊後轉到介紹頁面
        info_button_left = tk.Button(left_big_area, text="酒品種類與介紹", font=("Helvetica", 20), height=2, command=lambda: self.go_to_introduction())
        info_button_left.pack(side=tk.RIGHT, fill=tk.X)
        
        # 黑色粗線分隔符
        separator = tk.Frame(bottom_area, bg='black', width=5)
        separator.pack(side=tk.LEFT, fill=tk.Y)

        # 創建右大區
        right_big_area = tk.Frame(bottom_area)
        right_big_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 右大區的數據區
        data_text_right = """\
            啤酒溫度 (°C)：27 度
            托盤重量 (g)：350
            CO2 濃度 (g/L)：5.5
            累積出酒量 (L)：3.4"""
        data_area_right = tk.Label(right_big_area, text=data_text_right, anchor="w", font=("Helvetica", 20))
        data_area_right.pack(side=tk.LEFT, fill=tk.Y)
        
        # 右大區的按鈕區
        button_area_right = tk.Frame(right_big_area)
        button_area_right.pack(side=tk.RIGHT)

        # 創建"開始注酒"按鈕
        start_button_right = tk.Button(right_big_area, text="開始注酒", height=2, font=("Helvetica", 20))
        start_button_right.pack(side=tk.RIGHT, fill=tk.X)
        
        # 創建"停止注酒"按鈕
        stop_button_right = tk.Button(right_big_area, text="停止注酒", height=2, font=("Helvetica", 20))
        stop_button_right.pack(side=tk.RIGHT, fill=tk.X)
        
        # 創建"設定"按鈕，點擊後轉到設定頁面
        settings_button_right = tk.Button(right_big_area, text="設定", font=("Helvetica", 20), height=2, command=lambda: self.go_to_settings())
        settings_button_right.pack(side=tk.RIGHT, fill=tk.X)
        
        # 創建"酒品種類與介紹"按鈕，點擊後轉到介紹頁面
        info_button_right = tk.Button(right_big_area, text="酒品種類與介紹", font=("Helvetica", 20), height=2, command=lambda: self.go_to_introduction())
        info_button_left.pack(side=tk.RIGHT, fill=tk.X)

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
