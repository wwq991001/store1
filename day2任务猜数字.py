import random
import time

num = random.randint(0, 100)
print("已生成一个幸运数字（0-100），您每回有三次机会，如三次都错可退出或等10秒后再猜！")
count = 0
i = 0
while True:
    if i % 3 == 0 and i != 0:
        print('您已连续3次猜错，您可以退出或请稍等10s再猜')
        num2 = input("您还要继续吗？(y/n):")
        if num2 == 'y':
            print("请稍等")
            i = 0
            time.sleep(10)

        elif num2 == 'n':
            print('欢迎下次再来！')
            break
        else:
            print('别瞎输入！')
            continue

    num1 = int(input("请输入一个数字："))
    count += 1
    i += 1
    if num == num1:
        print("恭喜您猜对了，本次幸运数字为：", num)
        print("您已猜了", count, "次")
        print("欢迎下次再来！")
        break
    if num != num1:
        if num < num1 <= 100:
            print("猜大了")
            print("您已猜了", count, "次")
        elif num > num1 >= 0:
            print("猜小了")
            print("您已猜了", count, "次")
        elif num1 > 100 or num1 < 0:
            print("本次幸运数字范围为：0-100，请不要瞎猜！")
            print("您已猜了", count, "次")

