import tkinter as tk
from mainpage import MainPage
from settings import SettingsPage
from temperature import TemperaturePage

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Page Switching Example")
        
        self.frames = {}
        for F in (MainPage, SettingsPage, TemperaturePage):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainPage)
    
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
