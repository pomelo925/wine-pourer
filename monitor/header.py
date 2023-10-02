import tkinter as tk
from time import strftime

def create_top_bar(parent):
    # 深色背景
    top_bar = tk.Frame(parent, bg="black") 
    top_bar.pack(side=tk.TOP, fill=tk.X)
    
    # 深色背景，黃色文字
    software_name = tk.Label(top_bar, text="埔樂自動精釀生啤機軟體", bg="black", fg="yellow", height=2, font=("Helvetica", 20))  
    software_name.place(relx=0.5, rely=0.5, anchor='center')
    
    # 深色背景，黃色文字，靠右對齊
    time_label = tk.Label(top_bar, bg="black", fg="yellow", anchor='e', height=2, font=("Helvetica", 20)) 
    time_label.pack(side=tk.RIGHT, fill=tk.X) 
    update_time(time_label)


def update_time(label):
    label['text'] = strftime('%H:%M:%S %p')  # Set current time
    label.after(1000, update_time, label)  # Update every second
