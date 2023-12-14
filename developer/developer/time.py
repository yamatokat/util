# current_time_function.py
from datetime import datetime

def get_current_time():
    # 現在の時刻を取得
    current_time = datetime.now()
    # 時刻を文字列に変換して返す
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

# ファイルが直接実行された場合にだけ実行されるコード
if __name__ == "__main__":
    current_time = get_current_time()
    print("Current Time:", current_time)
