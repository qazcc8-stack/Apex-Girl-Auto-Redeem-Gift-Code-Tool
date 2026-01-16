import pyautogui
import pyperclip
import time
import os
import sys

# 檔案名稱設定
DATA_FILE = 'data.txt'
SETTING_FILE = 'pos_setting.txt'

def load_coordinates():
    """讀取 pos_setting.txt 並回傳兩個座標"""
    if not os.path.exists(SETTING_FILE):
        print(f"錯誤：找不到設定檔 '{SETTING_FILE}'")
        print("請建立檔案，第1行寫貼上座標(如 100,200)，第2行寫下個位置座標。")
        input("按 Enter 鍵離開...")
        sys.exit()

    try:
        with open(SETTING_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # 過濾掉空行
        lines = [line.strip() for line in lines if line.strip()]

        if len(lines) < 2:
            print(f"錯誤：'{SETTING_FILE}' 內容不足兩行！")
            sys.exit()

        # 解析座標函數 (處理中文逗號與空白)
        def parse_line(text):
            text = text.replace('，', ',') # 防止誤打中文逗號
            parts = text.split(',')
            return int(parts[0]), int(parts[1])

        pos_paste = parse_line(lines[0])
        pos_next = parse_line(lines[1])
        
        print(f"讀取設定成功：")
        print(f" -> 貼上位置: {pos_paste}")
        print(f" -> 下個位置: {pos_next}")
        return pos_paste, pos_next

    except Exception as e:
        print(f"讀取設定檔時發生錯誤：{e}")
        print("請檢查格式是否為 'x,y' (例如: 500,300)")
        input("按 Enter 鍵離開...")
        sys.exit()

def main():
    # 1. 先讀取座標
    pos_paste, pos_next = load_coordinates()

    # 2. 檢查資料檔
    if not os.path.exists(DATA_FILE):
        print(f"錯誤：找不到資料檔 '{DATA_FILE}'")
        input("按 Enter 鍵離開...")
        return

    print("\n=== 程式將在 5 秒後開始，請切換視窗 ===")
    time.sleep(5)

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for index, line in enumerate(lines):
        text = line.strip()
        if not text: continue

        print(f"[{index+1}] 處理中: {text}")

        # 複製
        pyperclip.copy(text)

        # 動作流程
        pyautogui.click(pos_paste)
        time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        pyautogui.click(pos_next)
        time.sleep(0.5)

    print("\n=== 全部完成 ===")
    input("按 Enter 鍵結束...")

if __name__ == "__main__":
    main()