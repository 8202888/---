import random

def 猜数字游戏():
    随机数 = random.randint(1, 100)
    尝试次数 = 0
    玩家猜测 = 0

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字。")

    while 玩家猜测 != 随机数:
        玩家猜测 = int(input("请输入你的猜测："))

        尝试次数 += 1
        if 玩家猜测 < 随机数:
            print("太低了！再试一次。")
        elif 玩家猜测 > 随机数:
            print("太高了！再试一次。")

    print(f"恭喜你！你猜对了数字 {随机数}，你总共尝试了 {尝试次数} 次。")

猜数字游戏()