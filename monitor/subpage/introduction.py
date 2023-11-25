import tkinter as tk
from tkinter import PhotoImage
from header import create_top_bar
from PIL import Image, ImageTk

class IntroductionPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        create_top_bar(self)

        self.content_frame = tk.Frame(self)  # 新增內部框架
        self.content_frame.pack(pady=20)  # 使用 pack 佈局管理器
        self.current_index = 0
        
        # 圖片和文字敘述的列表
        self.images = ["/home/pomelo/workspace/monitor/materials/a.png", 
                       "/home/pomelo/workspace/monitor/materials/b.png",
                       "/home/pomelo/workspace/monitor/materials/c.png"]
        self.titles = ["愛爾啤酒", "拉格啤酒", "精釀啤酒"]
        self.descriptions_paths = ["/home/pomelo/workspace/monitor/materials/a.txt", 
                           "/home/pomelo/workspace/monitor/materials/b.txt",
                           "/home/pomelo/workspace/monitor/materials/c.txt"]

        # 圖片顯示
        self.photo_image = Image.open(self.images[self.current_index])
        self.photo_image = self.photo_image.resize((432, 300), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo_image)
        
        self.image_label = tk.Label(self.content_frame, image=self.photo)
        self.image_label.grid(row=1, column=0, padx=10, pady=10)

        # 標題顯示
        self.title_label = tk.Label(self.content_frame, text=self.titles[self.current_index], font=("Arial", 20))
        self.title_label.grid(row=0, column=0, padx=10)

        # 文字敘述顯示
        description = self.read_description_from_file(self.descriptions_paths[self.current_index])
        self.desc_label = tk.Label(self.content_frame, text=description, wraplength=280, font=("Arial", 14), justify=tk.LEFT)
        self.desc_label.grid(row=1, column=1, padx=10, pady=10)

        # 切換按鈕
        self.prev_button = tk.Button(self.content_frame, text="上張", command=self.prev_image)
        self.prev_button.grid(row=2, column=0, pady=10, sticky='w')  

        self.next_button = tk.Button(self.content_frame, text="下張", command=self.next_image)
        self.next_button.grid(row=2, column=1, pady=10, sticky='e')  

        # 返回主頁面的按鈕
        button = tk.Button(self, text="Return", command=self.go_to_mainpage, height=5, font=("Arial", 20))
        button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def go_to_mainpage(self):
        from mainpage import MainPage
        self.controller.show_frame(MainPage)

    def prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.images)
        self.update_content()

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.images)
        self.update_content()

    def update_content(self):
        # 更新圖片
        self.photo_image = Image.open(self.images[self.current_index])
        self.photo_image = self.photo_image.resize((int(1080*0.4), int(600*0.5)), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo_image)
        self.image_label.config(image=self.photo)

        # 更新標題
        self.title_label.config(text=self.titles[self.current_index])

        # 更新文字敘述
        description = self.read_description_from_file(self.descriptions_paths[self.current_index])
        self.desc_label.config(text=description)
    
    def read_description_from_file(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
