import numpy as np

# 字典判断是根据键来判断
print('----------------------字典判断是根据键来判断----------------------------')
dict = {'地球': {'中国': {'北京': {'昌平': {'沙河': {'起码路': '北科院'}}}},
               '美国': '纽约'}, '火星': '沙漠'}
name = []
name.append(input("输入键："))
if name[0] in dict:
    print(dict['地球'])
    name.append(input("输入键："))
    if name[1] in dict['地球']:
        print(dict['地球']['中国'])
        name.append(input("输入键："))
        if name[2] in dict['地球']['中国']:
            print(dict['地球']['中国']['北京'])
            name.append(input("输入键："))
            if name[3] in dict['地球']['中国']['北京']:
                print(dict['地球']['中国']['北京']['昌平'])
                name.append(input("输入键："))
                if name[4] in dict['地球']['中国']['北京']['昌平']:
                    print(dict['地球']['中国']['北京']['昌平']['沙河'])
                    name.append(input("输入键："))
                    if name[5] in dict['地球']['中国']['北京']['昌平']['沙河']:
                        print(dict['地球']['中国']['北京']['昌平']['沙河']['起码路'])
                    else:
                        print('no')
                else:
                    print('no')
            else:
                print('no')
        else:
            print('no')
    else:
        print('no')

# 有下列人员数据库，请按要求实现
print('---------------------------有下列人员数据库，请按要求实现-----------------------')
print('姓名  年龄  性别  编号   任职公司   薪资   部门编号')
names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]]

num = []
for i in range(len(names)):
    print(names[i])
    num.append(names[i][5])

# 1.统计每个人的平均薪资
avg = np.mean(num)
print("平均薪资：", int(avg))

# 2.统计每个人的平均年龄
num1 = []
for k in range(len(names)):
    num1.append(int(names[k][1]))
avg = np.mean(num1)
print("平均年龄：", int(avg))

# 3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
names.append(['刘备', '45', '男', '220,', 'alibaba', 500, '30'])
for i in range(len(names)):
    print(names[i])

# 4.统计公司男女人数
count = count1 = 0
for i in names:
    if i[2] == '男':
        count += 1
    else:
        count1 += 1
print('公司男：', count, '人', '\t', '公司女：', count1, '人')
#
# count_person = []
# for l in names:
#     count_person.append(l[2])
# print(count_person.count('男'))

# 5.每个部门的人数
count_person1 = []
for l in names:
    count_person1.append((l[-1]))
print("部门为：", count_person1[0], '有：', count_person1.count('50'), '人')
print("部门为：", count_person1[1], '有：', count_person1.count('60'), '人')
print("部门为：", count_person1[3], '有：', count_person1.count('10'), '人')
print("部门为：", count_person1[4], '有：', count_person1.count('30'), '人')

# 现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
print('------------------------------魔法学院统计成绩--------------------------------')
num = {'罗恩': [23, 35, 44],
       '哈利': [60, 77, 68, 88, 90],
       '赫敏': [97, 99, 89, 91, 95, 90],
       '马尔福': [100, 85, 90]}

# 求每个人的总成绩？
for key in num:
    print(key, '总成绩：', sum(num[key]))

# 当输入是54321时，写出下面程序的执行结果
print('--------------------------------当输入是54321时，写出下面程序的执行结果-------------------')
num = int(input("请输入一个数："))
while num != 0:
    print(num % 10)
    num = num // 10

# # 结果： 1
#         2
#         3
#         4
#         5


# 请对下列列表进行冒泡排序
print('---------------------------------请对下列列表进行冒泡排序--------------------------')
a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
print(a)
a.sort(reverse=False)
print(a)
