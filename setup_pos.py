import pyautogui
import time
import os

FILENAME = 'pos_setting.txt'

def get_point(step_name):
    """引導使用者取得單一座標"""
    print(f"\n--- 設定步驟：{step_name} ---")
    print(f"請將滑鼠移動到【{step_name}】的位置...")
    input(">> 移動好後，請按 Enter 鍵確認...")
    
    x, y = pyautogui.position()
    print(f"✅ 已捕捉座標: {x}, {y}")
    return x, y

def main():
    print("=== 自動化座標設定工具 ===")
    print("本程式將協助你產生座標設定檔。")
    print("------------------------------")

    # 1. 取得第一個點
    p1_x, p1_y = get_point("貼上文字的位置 (位置 A)")
    
    # 2. 取得第二個點
    time.sleep(0.5) # 防止誤觸
    p2_x, p2_y = get_point("點擊下一個的位置 (位置 B)")

    # 3. 儲存檔案
    try:
        content = f"{p1_x},{p1_y}\n{p2_x},{p2_y}"
        
        with open(FILENAME, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("\n" + "="*30)
        print(f"🎉 設定成功！檔案已儲存為 {FILENAME}")
        print(f"內容預覽：\n{content}")
        print("="*30)
        
    except Exception as e:
        print(f"\n❌ 存檔失敗：{e}")

    input("\n按 Enter 鍵結束程式...")

if __name__ == "__main__":
    main()