import threading

# 初期値
a = 1
b = 5

# aとbを変更する関数
def update_a():
    global a
    for i in range(5):
        a = a + 2
        a = a + a
        a = b
        c = a + b
        print("✕", a)

def update_b():
    global b
    for g in range(10):
        b = b + a
        print("♡", b)

# スレッドを作成
thread1 = threading.Thread(target=update_a)
thread2 = threading.Thread(target=update_b)

# スレッドを開始
thread1.start()
thread2.start()

# スレッドの終了を待つ
thread1.join()
thread2.join()

print("最終的な a:", a)
print("最終的な b:", b)
