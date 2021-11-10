'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
任务：优惠券加上随机获得一张优惠券（9折10，5折3，免费的1：单个商品打折9折10，5折3，免费的1）
'''
# 准备商品

import random

shop = [
    #     0   ,   1
    ["戴尔", 19999],  # 0
    ["电磁炉", 199],  # 1
    ["A4纸", 9.9],  # 2
    ["华为P50 4G", 5000],  # 3
    ["iphone 13", 5788],
    ['养生壶', 200],
    ['笔', 2]
]

transfer = [[0.9, 10],
            [0.5, 3],
            [0, 1],
            [0.9, 10],
            [0.5, 3],
            [0, 1]
            ]

# 初始化余额
money = input("请输入您的余额")
money = int(money)
# 准备一个购物车
mycart = []
# 随机抽取优惠券
random2 = int(len(transfer))
random1 = random.randint(0, random2 - 1)
if random1 <= 2:
    print("恭喜，抽到了团购！这是你的优惠券：", transfer[random1])
    while True:
        # 展示商品
        for index, value in enumerate(shop):
            print(index, ":", value)
        chose = list(input("请输入商品编号").split())  # 输入的还是str
        for i in range(len(chose)):
            if chose[i].isdigit():
                chose[i] = int(chose[i])
                if chose[i] > len(shop) - 1:
                    print("这里没有您需要的商品")
                    break
                else:
                    continue
            elif chose == ["q"] or chose == ["Q"]:
                # 打印购物小条
                print("=====================")
                for index, value in enumerate(mycart):
                    print(index, ":", value, )
                    print("您的余额还剩:", money)
                    break
            else:  # 不是数字
                print("输入错误")
                #   余额满足的条件
        else:
            if all(v < money for v in chose):
                if transfer[random1][1] > 0:
                    for j in range(len(chose)):
                        mycart.append(shop[chose[j]])
                        money = money - shop[chose[j]][1] * transfer[random1][0]
                    transfer[random1][1] -= 1
                    print("恭喜你，加入购物车，您的余额为：", money)
                else:
                    for j in range(len(chose)):
                        mycart.append(shop[chose[j]])
                        money = money - shop[chose][j][1]
                    print("恭喜你，加入购物车，您的余额为：", money)


else:
    print("恭喜，抽到了单购！这是你的优惠券：", transfer[random1])
    while True:
        # 展示商品
        for index, value in enumerate(shop):
            print(index, ":", value)
        chose = input("请输入商品编号")  # 输入的还是str
        if chose.isdigit():  # 判断是否是数字
            chose = int(chose)
            if chose > len(shop) - 1:
                print("这里没有您需要的商品")
            else:
                #   余额满足的条件
                if 0 < shop[chose][1] < money:
                    if transfer[random1][1] > 0:
                        mycart.append(shop[chose])
                        money = money - shop[chose][1] * transfer[random1][0]
                        transfer[random1][1] -= 1
                        print("恭喜你，加入购物车，您的余额为：", money)
                    else:
                        mycart.append(shop[chose])
                        money = money - shop[chose][1]
                        print("恭喜你，加入购物车，您的余额为：", money)
                # 不满足
                else:
                    print("gun")
        elif chose == "q" or chose == "Q":
            #    打印购物小条
            print("=====================")
            for index, value in enumerate(mycart):
                print(index, ":", value, )
            print("您的余额还剩:", money)
            break
        else:  # 不是数字
            print("输入错误")

import pprint
from typing import List

dict1 = {"k1": "v1", "k2": "v2", "k3": "v3"}
# 1、请循环遍历出所有的key
print("-------请循环遍历出所有的key-----------")
for key in dict1:
    print(key)
# 2、请循环遍历出所有的value
print('---------请循环遍历出所有的value------')
for key in dict1:
    print(dict1[key])

# 3、请在字典中增加一个键值对,"k4":"v4"
print('--------请在字典中增加一个键值对,"k4":"v4"--------')
dict1['k4'] = 'v4'
print(dict1)

'''小明去超市购买水果，账单如下
苹果  32.8
香蕉  22
葡萄  15.5
请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
用水果名称做key，金额做value，创建一个字典'''
info = {
    '苹果': 32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
'''小明，小刚去超市里购买水果
小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
以姓名做key，value仍然是字典'''

Friuts = {
    '苹果': 12.3,  # 水果和单价
    '草莓': 4.5,
    '香蕉': 6.3,
    '葡萄': 5.8,
    '橘子': 6.4,
    '樱桃': 15.8
}

info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': Friuts['苹果'] * 4 + Friuts['草莓'] * 13 + Friuts['香蕉'] * 10
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': Friuts['葡萄'] * 19 + Friuts['橘子'] * 12 + Friuts['樱桃'] * 30
    }
}
print(info)


# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）


def add(num: List[int]):
    num3 = dict()
    for i in num:
        if num.count(i) not in num3:
            num3[i] = num.count(i)
    return num3


lii = [21, 21, 21, 56, 10, 10, 56, 10, 56, 56, 56, 56, 56, 56, 56]
print(add(lii))

# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700, "10"]
]

a_dict = dict()
for i in names:
    a_dict[i[0]] = i[1:]
print("姓名  年龄  性别  编号   任职公司   薪资   部门编号")
pprint.pprint(names)
print("姓名  年龄  性别  编号   任职公司   薪资   部门编号")
pprint.pprint(a_dict)

# 各组，开始分析《中国工商银行账户管理系统》需求
'''
    准备一个空的数据库(能存储100用户的库(字典)
    银行名称:中国工商银行的昌平支行(str 写死的！）
'''
# 2.进入时的界面显示
'''
***********************************************************************
*                      中国工商银行的昌平支行                            *
 *                         账户管理系统                                *
*                            V1.0                                    *
***********************************************************************

*1.开户
*2.存钱
*3.取钱
*4.转账
*5.查询
*6.Bye！
'''

# 3.银行的开户逻辑（传入参数：用户的所有信息。返回值：整型值）
'''
用户的所有信息约束：
    账号（str：系统随机产生8位数字）
    姓名(str)
    密码(int:6位数字)
    地址
    存款余额(int)
    开户行（银行的名称（str））写死的！
''''''
判断该用户的账号在库里是否存在：
    不存在则在用户库里添加一个该用户并返回代号1
    若存在则返回代号2
''''''
   添加用户是判断用户库是否已注册满：
        若已满则返回代号3
'''
# 4.银行的存钱逻辑（传入值：用户的账号、存取的金额。返回值：布尔类型值）
'''根据传入的账号信息查询用户库里是否有该用户：若没有则返回False，若有，则将该用户的金额存进去。
'''
# 5.银行的取钱逻辑（传入值：用户的账号，用户密码，取钱金额。返回值：整型值）
'''
    查询该用户是否存在：
        若不存在，则返回代号1，
        若存在，则继续判断密码是否正确：
            若不正确，则返回代号2。
            若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱：
            若不满足，则返回代号3，
            若满足，则将该用户的金额减去。
'''
# 6.银行的转账逻辑（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
'''
    先查询用户库是否存在转出和转入的账号:
        若不存在则返回代号:1
        若账号都存在则继续判断转出账号的密码是否正确:
            若不正确，则返回2
            若正确则继续判断要转出的金额是否足够:
                若不够则返回3
	            否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。
'''
# 7.银行的查询账户逻辑（传入值：账号，账号密码，返回值：空）
'''
    先根据账号判断用户库是否存在该用户:
        若不存在则打印提示信息：该用户不存在。
        否则继续判断密码是否正确:
            若不正确则打印相对应的错误信息。
            若账号和密码都正确，则将该用户的信息都打印出来:
                比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
'''
# 8.正式开始业务
