import tkinter as tk  
import os
import csv
from header import create_top_bar
from tkinter import messagebox 
from time import strftime

##############
# 資料處理流程 #
##############

def get_csv_path():
    # 獲取當前腳本的目錄
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 獲取上級目錄
    parent_dir = os.path.dirname(script_dir)
    # 構造csv文件的完整路徑
    csv_path = os.path.join(parent_dir, 'esp32', 'current.csv')
    return csv_path

# 從 csv 中讀取資料
def read_value_from_csv(column_name):
    with open(get_csv_path(), mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row[column_name]
    
# 更新變數(右)
def update_data_text_right():
    # beer_temperature_right = read_value_from_csv('啤酒溫度')
    beer_temperature_right = 1
    tray_weight_right = read_value_from_csv('重量')
    co2_concentration_right = read_value_from_csv('壓力')
    # co2_concentration_right = 1
    # cumulative_liquor_volume_right = read_value_from_csv('累積出酒量')
    cumulative_liquor_volume_right = 1

    data_text_right = f"""
\n啤酒溫度 (°C)：{beer_temperature_right}  托盤重量 (g)：{tray_weight_right}
氣壓 (kPa)：{co2_concentration_right}   累積出酒量 (L)：{cumulative_liquor_volume_right}     \n"""

    return data_text_right

# 更新變數(左)
def update_data_text_left():
    # beer_temperature_left = read_value_from_csv('啤酒溫度')
    beer_temperature_left = 1
    tray_weight_left = read_value_from_csv('重量')
    co2_concentration_left = read_value_from_csv('壓力')
    # co2_concentration_left = 1
    # cumulative_liquor_volume_left = read_value_from_csv('累積出酒量')
    cumulative_liquor_volume_left = 1

    data_text_left = f"""
\n啤酒溫度 (°C)：{beer_temperature_left}  托盤重量 (g)：{tray_weight_left}
氣壓 (kPa)：{co2_concentration_left}   累積出酒量 (L)：{cumulative_liquor_volume_left}     \n"""

    return data_text_left


# 開始注酒視窗
def on_start_button_click():
    # Replace this with your actual logic to check if the cup is placed
    cup_placed = True  # Example condition
    if cup_placed:
        messagebox.showinfo("Info", "準備倒酒 ... 請勿移動酒杯 ...")
    else:
        messagebox.showerror("Error", "未偵測到重量，請先放置酒杯！")


# 停止注酒視窗
def on_stop_button_click():
   messagebox.showinfo("Info", "已停止注酒，可取走酒杯。")


##############
# 前端頁面設計 #
##############

# 定義主頁面類別
class MainPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)  # 初始化 Frame
        self.controller = controller  # 設定控制器

#######
# 頂底 #
#######
        ## 創建標題列
        create_top_bar(self)

        ## 創建底部按鈕："酒品種類與介紹"，點擊後轉到介紹頁面
        info_button = tk.Button(self, text="酒品種類與介紹", font=("Helvetica", 25), height=2, command=lambda: self.go_to_introduction())
        info_button.pack(side=tk.BOTTOM, fill=tk.X)

        ## 創建底部區域
        bottom_area = tk.Frame(self)
        bottom_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        half_screen_width = int(self.winfo_screenwidth() / 2)

#######
# 左區 #
#######
        # 創建左大區
        left_big_area = tk.Frame(bottom_area, width=half_screen_width)
        left_big_area.pack(side=tk.LEFT, fill=tk.BOTH)

        # 左上數據區 Frame
        data_frame_left = tk.Frame(left_big_area)
        data_frame_left.grid(row=0, column=0)

        # 左上數據區
        self.data_area_left = tk.Label(data_frame_left, anchor="w", font=("Helvetica", 18))
        self.data_area_left.pack(side=tk.TOP, fill=tk.BOTH)

        # 左下按鈕區 Frame
        button_frame_left = tk.Frame(left_big_area)
        button_frame_left.grid(row=1, column=0)

        # 創建"開始注酒"按鈕
        start_button_left = tk.Button(button_frame_left, text="開始注酒", height=2, font=("Helvetica", 25), command=on_start_button_click)
        start_button_left.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"停止注酒"按鈕
        stop_button_left = tk.Button(button_frame_left, text="停止注酒", height=2, font=("Helvetica", 25), command=on_stop_button_click)
        stop_button_left.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"設定"按鈕，點擊後轉到設定頁面
        settings_button_left = tk.Button(button_frame_left, text="設定", font=("Helvetica", 25), height=2, command=lambda: self.go_to_settings())
        settings_button_left.pack(side=tk.TOP, fill=tk.X)
        
        # 黑色粗線分隔符
        separator = tk.Frame(bottom_area, bg='black', width=5)
        separator.pack(side=tk.LEFT, fill=tk.Y)

#######
# 右區 #
#######
        ## 創建右大區
        right_big_area = tk.Frame(bottom_area, width=half_screen_width)
        right_big_area.pack(side=tk.TOP, fill=tk.BOTH)
        
        # 右上數據區 Frame
        data_frame_right = tk.Frame(right_big_area)
        data_frame_right.grid(row=0, column=0)

        # 右上數據區
        self.data_area_right = tk.Label(data_frame_right, anchor="w", font=("Helvetica", 18))
        self.data_area_right.pack(side=tk.TOP, fill=tk.BOTH)

        # 右下按鈕區 Frame
        button_frame_right = tk.Frame(right_big_area)
        button_frame_right.grid(row=1, column=0)

        # 創建"開始注酒"按鈕
        start_button_right = tk.Button(button_frame_right, text="開始注酒", height=2, font=("Helvetica", 25), command=on_start_button_click)
        start_button_right.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"停止注酒"按鈕
        stop_button_right = tk.Button(button_frame_right, text="停止注酒", height=2, font=("Helvetica", 25), command=on_stop_button_click)
        stop_button_right.pack(side=tk.TOP, fill=tk.X)
        
        # 創建"設定"按鈕，點擊後轉到設定頁面
        settings_button_right = tk.Button(button_frame_right, text="設定", font=("Helvetica", 25), height=2, command=lambda: self.go_to_settings())
        settings_button_right.pack(side=tk.TOP, fill=tk.X)

        # 定期更新數據
        self.update_data_areas()

#######
# 函式 #
#######

    # 更新數據區
    def update_data_areas(self):
        # 更新左上數據區 
        data_text_left = update_data_text_left()  
        self.data_area_left.config(text=data_text_left)

        # 更新右上數據區 
        data_text_right = update_data_text_right()
        self.data_area_right.config(text=data_text_right)

        # 每秒運行一次
        self.after(1000, self.update_data_areas)


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
