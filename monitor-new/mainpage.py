import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="This is the main page")
        label.pack()
        
        button = tk.Button(self, text="Settings",
                           command=lambda: self.go_to_settings())
        button.pack()

    def go_to_settings(self):
        from settings import SettingsPage
        self.controller.show_frame(SettingsPage)
