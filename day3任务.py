'''
随机生成一个处罚遍数
    选择容器：
    元组：（1,2,3）#他是不可修改而且是唯一
    列表：[1,2,3] # 他是可以修改的
有一个列表里面有人名
优化代码：一个输入进行判断，判断为1 开始选人，判断为2开始生成数字  判断为q Q，退出
'''
import random
import numpy as np
import time
import math


print("============欢迎来到处罚系统===============")
list = ["陆梓言", "郭洪波", "方则属", "签", "千纸鹤", "EXO"]
while True:
    inex = input("输入1开始选人/输入2开始生成处罚编数/输入q\Q退出:")
    if inex == '1':
        ran = random.randint(0, len(list) - 1)  # len==6  范围是0-6全部可以取到
        print("恭喜", list[ran], "被选中了")
    elif inex == '2':
        num = random.randint(0, 90)
        print(list[ran], "处罚了", num, "遍")
    elif inex == 'q' or inex == 'Q':
        print("欢迎下次再来！")
        break

# 实现输入10个数字，并打印10个数的求和结果
print("------------------实现输入10个数字，并打印10个数的求和结果------------------------")
while True:
    num = list(map(float, input("请输入10个数：").split()))
    if len(num) > 10 or len(num) < 10:
        print("请输入10个数！")
    else:
        print('输入的10个数的和为：', sum(num))
        break

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
print('-----------从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。--------------')
num = []
for i in range(10):
    num.append(eval(input("请依次输入10个数:")))

avg = np.mean(num)
print("10个数的最大值", max(num))
print("10个数的和：", sum(num))
print('10个数的平均数', avg)

使用random模块，如何产生 50~150之间的数？
print("-------------------使用random模块，如何产生 50~150之间的数？------------------")
num = random.uniform(50, 150)
print("随机数：", num)

# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
print("-----------从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形------------")
while True:
    a = input("输入y:开始/继续|输入n:停止 ：")
    if a == 'n':
        print("欢迎下次再来！")
        break
    elif a == 'y':
        a_list = list(map(float, input("请输入三条边：").split()))
        if len(a_list) == 3:
            if a_list[0] + a_list[1] > a_list[2] and a_list[0] + a_list[2] > a_list[1] and a_list[1] + a_list[2] > a_list[0]:
                if a_list[0] == a_list[1] != a_list[2] or a_list[0] == a_list[2] !=a_list[1] or a_list[1] == a_list[2] != a_list[0]:
                    if a_list[0] ** 2 + a_list[1] ** 2 != a_list[2] ** 2 or a_list[0] ** 2 + a_list[2] ** 2 != a_list[1] ** 2 or a_list[1] ** 2 + a_list[2] ** 2 != a_list[0] ** 2:
                        print("可以形成等腰三角形！")
                elif a_list[0] == a_list[1] == a_list[2]:
                    print("可以形成等边三角形！")
                elif a_list[0] ** 2 + a_list[1] ** 2 == a_list[2] ** 2 or a_list[0]**2 + a_list[2]**2 ==a_list[1]**2 or a_list[1]**2 +a_list[2] ** 2 == a_list[0] **2:
                    if a_list[0] != a_list[1] != a_list[2]:
                        print("可以形成直角三角形！")
                    else:
                        print("可以形成等腰直角三角形！")
                else:
                    print("可以形成普通三角形！")
            else:
                print("不能构成三角形！")
        else:
            print("请输入三条边！")
            continue
    else:
        print("请正常输入！")
        continue

'''
有以下两个数，使用+，-号实现两个数的调换。
               A=56
               B=78
实现效果：
               A=78
               B=56
'''
print("---------------------使用+，-号实现两个数的调换---------------------")
A, B, C= 56, 78, 22
print("A=",A+C,"B=",B-C)
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
print("-------------------欢迎使用本系统-------------------")
data = {'用户名': 'root', '密码': 'admin', '锁定': 0, 'cnt': 1}

flag = 0
while True:
    user_name = input("请输入您的用户名：")
    user_pwd = input("请输入您的密码：")
    if data['锁定'] == 1:
        num = input('用户已锁定！想恢复找你系统爸爸！(退出系统：q/Q)')
        if num =='q' or num=='Q':
            break
        else:
            time.sleep(9999999)
    elif data['锁定'] == 0:
        if data["用户名"] == user_name and data['密码'] == user_pwd:
            print("登录成功！")
            break
        elif data["用户名"] != user_name or data['密码'] != user_pwd:
            print('用户名或密码错误！')
            if data['cnt'] == 3:
                data['锁定'] = 1
                num = input('用户已锁定！想恢复找你系统爸爸！(退出系统：q/Q)')
                if num == 'q' or num == 'Q':
                    break
                else:
                    time.sleep(9999999)
            data['cnt'] += 1
        else:
            continue
    else:
        time.sleep(9999999)


# *号金字塔
print("------------------------------*号金字塔--------------------------------")
a =eval(input("输入金字塔层数："))
if a >= 0:
    for i in range(1, a+1):
        b = (2*a - i)
        print(' ' * b, '* ' * i, )
else:
    print('不能输入负数！')


# 使用while循环实现99乘法表的打印。
print('------------------------使用while循环实现99乘法表的打印----------------')
b = 1
while b <= 9:
    a = 1
    while a <= b:
        print("{0}*{1}={2:2d}".format(a, b, a*b), end=' ')
        a += 1
    print("")
    b += 1


# 编程实现99乘法表的倒叙打印
print('-----------------------编程实现99乘法表的倒叙打印--------------------------')
for i in range(9,0, -1):
    for j in range(1,i+1):
        print("{0}*{1}={2:2d}".format(j, i, i*j), end=' ')

    print(' ')


# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
print('---- 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？----')
day = 0
for i in range(20):
    i += 3
    day += 0.5
    print('第', day, '白天爬到了：', i, 'm')
    if i >= 20:
        break
    else:
        day += 0.5
        i -= 2
        print('第', day, '夜晚爬到了：', i, 'm')
print('用了', day, '天爬出来。')


# 判断下列变量命名是否合法
variate = ['char', 'Oax_li', 'fLul', 'BYTE', 'Cy%ty', '$123', '3_3', 'T_T']
for i in variate:
    if i[0].isalpha() or i[0] =='_':
        for j in i[1:]:
            if not(j.isalnum() or j == '_'):
                print("变量名不合法！")
                falg = False
                break
        else:
            print("变量名合法!")

    else:
        print("变量名不合法！")


'''
继续完成上午的猜数字游戏的需求功能。
    1.	添加计数打印功能
    2.	添加次数金币功能和锁定系统功能
'''

num = random.randint(0, 100)
money = eval(input("请输入金币数量："))
print("已生成一个幸运数字（0-100），您每回有三次机会，每次猜错扣金币：500，猜对加金币：3000，如三次都错可退出或等10秒后再猜！")
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
            print('欢迎下次再来！您已猜:', count, '次', '本次剩余金币数量:', money)
            break
        else:
            print('别瞎输入！')
            continue

    num1 = int(input("请输入一个数字："))
    count += 1
    i += 1
    if num == num1:
        print("恭喜您猜对了，本次幸运数字为：", num)
        money += 3000
        print("您已猜了", count, "次", '本次还剩金币数量：', money)
        print("欢迎下次再来！")
        break
    else:
        if num < num1 <= 100:
            print("猜大了")
            money -= 500
            print("您已猜了", count, "次", '本次还剩金币数量：', money)
        elif num > num1 >= 0:
            print("猜小了")
            money -= 500
            print("您已猜了", count, "次", '本次还剩金币数量：', money)
        elif num1 > 100 or num1 < 0:
            print("本次幸运数字范围为：0-100，请不要瞎猜！")
            money -= 500
            print("您已猜了", count, "次", '本次还剩金币数量：', money)


#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
print("-----------------用循环来实现20以内的数的阶乘------------------------")
value = []
for i in range(1,21):
    value.append(math.factorial(i))
    print(i, '! =', value[i-1])
print("1! +2!+3!+…..+20! =", sum(value))




