import csv
import os

# 獲取當前腳本的目錄
script_dir = os.path.dirname(os.path.abspath(__file__))

# 將腳本目錄與文件名連接起來以獲得完整的路徑
csv_path = os.path.join(script_dir, 'current.csv')

# 讀取 Arduino 資訊，撰寫到 csv 中
def read_weight_from_csv():
    with open(csv_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # 跳過標題行
        weight = next(reader)[0]
        return float(weight)
    

if __name__ == "__main__":
    weight = read_weight_from_csv()
    print(f'重量: {weight}')
