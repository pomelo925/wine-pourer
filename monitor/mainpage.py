import tkinter as tk  
from header import create_top_bar 
from time import strftime

# 定義主頁面類別
class MainPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)  # 初始化 Frame
        self.controller = controller  # 設定控制器
        
        ## 創建標題列
        create_top_bar(self)

        ## 創建底部按鈕："酒品種類與介紹"，點擊後轉到介紹頁面
        info_button = tk.Button(self, text="酒品種類與介紹", font=("Helvetica", 25), height=2, command=lambda: self.go_to_introduction())
        info_button.pack(side=tk.BOTTOM, fill=tk.X)

        ## 創建底部區域
        bottom_area = tk.Frame(self)
        bottom_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        half_screen_width = int(self.winfo_screenwidth() / 2)

        # 創建左大區
        left_big_area = tk.Frame(bottom_area, width=half_screen_width)
        left_big_area.pack(side=tk.LEFT, fill=tk.BOTH)

        # 左上數據區 Frame
        data_frame_left = tk.Frame(left_big_area)
        data_frame_left.grid(row=0, column=0)

        data_text_left = """\
\n啤酒溫度 (°C)：27  托盤重量 (g)：350
CO2濃度 (g/L)：5.5   累積出酒量 (L)：3.4     \n"""
        data_area_left = tk.Label(data_frame_left, text=data_text_left, anchor="w", font=("Helvetica", 18))
        data_area_left.pack(side=tk.TOP, fill=tk.BOTH)

        # 左下按鈕區 Frame
        button_frame_left = tk.Frame(left_big_area)
        button_frame_left.grid(row=1, column=0)

        # 創建"開始注酒"按鈕
        start_button_left = tk.Button(button_frame_left, text="開始注酒", height=2, font=("Helvetica", 25))
        start_button_left.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"停止注酒"按鈕
        stop_button_left = tk.Button(button_frame_left, text="停止注酒", height=2, font=("Helvetica", 25))
        stop_button_left.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"設定"按鈕，點擊後轉到設定頁面
        settings_button_left = tk.Button(button_frame_left, text="設定", font=("Helvetica", 25), height=2, command=lambda: self.go_to_settings())
        settings_button_left.pack(side=tk.TOP, fill=tk.X)
        
        # 黑色粗線分隔符
        separator = tk.Frame(bottom_area, bg='black', width=5)
        separator.pack(side=tk.LEFT, fill=tk.Y)

        ## 創建右大區
        right_big_area = tk.Frame(bottom_area, width=half_screen_width)
        right_big_area.pack(side=tk.TOP, fill=tk.BOTH)
        
        # 右上數據區 Frame
        data_frame_right = tk.Frame(right_big_area)
        data_frame_right.grid(row=0, column=0)

        data_text_right = """\
\n啤酒溫度 (°C)：32  托盤重量 (g)260
CO2濃度 (g/L)：5.6 累積出酒量 (L)：1.9\n"""
        data_area_right = tk.Label(data_frame_right, text=data_text_right, anchor="w", font=("Helvetica", 18))
        data_area_right.pack(side=tk.TOP, fill=tk.BOTH)

        # 右下按鈕區 Frame
        button_frame_right = tk.Frame(right_big_area)
        button_frame_right.grid(row=1, column=0)

        # 創建"開始注酒"按鈕
        start_button_right = tk.Button(button_frame_right, text="開始注酒", height=2, font=("Helvetica", 25))
        start_button_right.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"停止注酒"按鈕
        stop_button_right = tk.Button(button_frame_right, text="停止注酒", height=2, font=("Helvetica", 25))
        stop_button_right.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"設定"按鈕，點擊後轉到設定頁面
        settings_button_right = tk.Button(button_frame_right, text="設定", font=("Helvetica", 25), height=2, command=lambda: self.go_to_settings())
        settings_button_right.pack(side=tk.TOP, fill=tk.X)
        
    
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
