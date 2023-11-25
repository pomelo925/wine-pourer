# 開發用
## 新增介面
### 步驟 1: 創建新的 Frame 子類
創建一個新的 Python 文件（例如 newpage.py）並定義一個新的 Frame 子類。
這個子類應該包含該介面所有的 widgets 和跳轉邏輯。

```python=
# newpage.py
import tkinter as tk

class NewPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="This is the new page")
        label.pack()
        
        button = tk.Button(self, text="Return",
                           command=self.go_to_main)
        button.pack()

    def go_to_main(self):
        from mainpage import MainPage
        self.controller.show_frame(MainPage)
```


### 步驟 2: 更新主程序
在主程序（通常是 app.py）中，將這個新的 Frame 子類加入到 self.frames 字典中。
```python=
# 在其他 imports 後面加上
from newpage import NewPage

# 在 App 類的 __init__ 方法中
for F in (MainPage, SettingsPage, TempPage, NewPage):  # 添加 NewPage
    frame = F(self, self)
    self.frames[F] = frame
    frame.grid(row=0, column=0, sticky="nsew")
```

### 步驟 3: 添加跳轉邏輯
在其他介面（如 MainPage、SettingsPage 或 TempPage）中，添加一個或多個按鈕或其他控件，以便用戶可以跳轉到這個新的介面。
```python=
# 例如，在 MainPage 中
button = tk.Button(self, text="New Page",
                   command=self.go_to_mainpage)
button.pack()

# 添加一個新方法來處理跳轉
def go_to_mainpage(self):
    from subpage.settings import SettingsPage
    self.controller.show_frame(SettingsPage)
```