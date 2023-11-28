# 埔樂自動精釀生啤機軟體
## A. 軟體安裝說明
確保樹梅派已安裝 Ubuntu 20.04 或 22.04 後，遵循以下步驟安裝。

1. 瀏覽至本地資料夾中，開啟終端機輸入以下指令安裝。

    ```
    git clonehttps://github.com/pomelo925/wine-pourer-rpi.git
    ```
2. 進入資料夾 `wine-pourer-rpi`：
    ```
    cd wine-pourer-rpi
    ```
3. 給予腳本 `install.sh` 權限：
    ```
    chmod +x install.sh
    ```
4. 執行腳本，安裝環境。
    ```
    ./install.sh
    ```
5. 執行程式腳本，開啟啤酒操作互動介面。
    ```
    ./app.sh
    ```


## B. 資料夾結構
以下為此 repository 之資料結構說明，大部分程式碼中有註解。
```py
├── esp32/  ## 與 esp32 通訊 
    └── current.csv/  # 紀錄當前 ESP32 傳遞資訊
    └── write_fromESP32/  # 資訊流： ESP32 -> 螢幕介面 
    └── write_toESP32/ # 資訊流： 螢幕介面 -> ESP32  
├── monitor/  ## 螢幕介面
    # 資料夾
    └── _pycache_/ 
    └── materials/  # 啤酒圖文介紹
    └── subpage/  # 子頁面(首層)
    └── subsubpage/  # 子頁面(第二層)
        └── _pycache_/ 
        └── _init__.py
        └── alcoholAngle.py  #  介面設計：出酒角度設定頁面
        └── ...
    # 檔案
    └── _init__.py
    └── app.py  
    └── header.py  # 介面設計：視窗最上方之橫條
    └── mainpage.py  # 定義介面邏輯
    └── settings.csv  # 設定檔
├── .gitignore
├── app.sh  # 執行軟體程序
├── install.sh  # 安裝軟體之依賴環境 (只須執行一次 )
├── README.md
``` 



## C. 開發指引 — 新增使用者介面
### C-1 : 創建新的 Frame 子類
創建一個新的 Python 文件（如 `newpage.py`）並自定義新的 `Frame` 子類。
這個子類應該包含該介面所有的  `widgets` 和跳轉邏輯。

```py
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


### C-2 : 更新主程序
在主程序（通常是 `app.py`）中，將此新的 `Frame` 子類加入到 `self.frames` 字典中。
```py
# 在其他 imports 後面加上
from newpage import NewPage

# 在 App 類的 __init__ 方法中
for F in (MainPage, SettingsPage, TempPage, NewPage):  # 添加 NewPage
    frame = F(self, self)
    self.frames[F] = frame
    frame.grid(row=0, column=0, sticky="nsew")
```

### C-3: 添加跳轉邏輯
在其他介面（如 `MainPage`、`SettingsPage`、 `TempPage`）中，添加一個或多個按鈕或其他控件，以便用戶可以跳轉到這個新的介面。

```py
# 例如，在 MainPage 中
button = tk.Button(self, text="New Page",
                   command=self.go_to_mainpage)
button.pack()

# 添加一個新方法來處理跳轉
def go_to_mainpage(self):
    from subpage.settings import SettingsPage
    self.controller.show_frame(SettingsPage)
```

