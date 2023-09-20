import tkinter as tk
from header import create_top_bar

class IntroductionPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        create_top_bar(self)

        label = tk.Label(self, text="This is introduction page.")
        label.pack()
        
        button = tk.Button(self, text="Return",
                           command=self.go_to_mainpage)
        button.pack()

    def go_to_mainpage(self):
        from mainpage import MainPage
        self.controller.show_frame(MainPage)

