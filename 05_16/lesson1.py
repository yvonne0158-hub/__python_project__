import random


def play_guess_number():
    """簡單的猜數字遊戲。"""
    secret_number = random.randint(1, 100)
    max_attempts = 10

    print("歡迎來到猜數字遊戲！")
    print("我已選好一個 1 到 100 之間的數字。你有 10 次機會猜中它。")

    for attempt in range(1, max_attempts + 1):
        while True:
            guess_text = input(f"第 {attempt} 次，請輸入你的猜測：")
            if not guess_text.isdigit():
                print("請輸入一個有效的整數。")
                continue

            guess = int(guess_text)
            if guess < 1 or guess > 100:
                print("請輸入介於 1 到 100 的數字。")
                continue

            break

        if guess == secret_number:
            print(f"恭喜你！猜對了，答案就是 {secret_number}！")
            return
        elif guess < secret_number:
            print("太小了，再試一次。")
        else:
            print("太大了，再試一次。")

        remaining = max_attempts - attempt
        if remaining:
            print(f"你還有 {remaining} 次機會。\n")

    print(f"很遺憾，次數用完了。答案是 {secret_number}。")


if __name__ == "__main__":
    play_guess_number()
