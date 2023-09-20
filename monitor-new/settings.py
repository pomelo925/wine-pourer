import tkinter as tk

class SettingsPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="This is the settings page")
        label.pack()
        
        button1 = tk.Button(self, text="Return",
                            command=self.go_to_main)
        button1.pack()
        
        button2 = tk.Button(self, text="Temp",
                            command=self.go_to_temp)
        button2.pack()

    def go_to_main(self):
        from mainpage import MainPage
        self.controller.show_frame(MainPage)

    def go_to_temp(self):
        from temperature import TemperaturePage
        self.controller.show_frame(TemperaturePage)
