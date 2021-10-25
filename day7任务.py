import xlrd
import numpy as np
import collections as d

wb = xlrd.open_workbook(filename="E:\\PYthon自动化测试\\python\\python任务\\day7\\任务\\2020年每个月的销售情况.xlsx",
                        encoding_override=True)
df = wb.sheet_names()
st = dict()
rows = list()
# 每月工作表
for i in range(len(df)):
    st[i + 1] = wb.sheet_by_index(i)
# 每月总行数
for j in range(len(df)):
    rows.append(st[j + 1].nrows)
# 总列数
cols = st[1].ncols

# 年销售总额
sal1 = list()
sal_sum = 0
for i in st.keys():
    sal2 = list()
    for j in range(1, rows[i-1]):
        data = st[i].row_values(j)
        sal2.append(data[2]*data[4])
    sal1.append(sum(sal2))
    print('%s月销售总额：%d' % (i, sal1[i-1]))
print('年销售总额：', "{:.2f}".format(sum(sal1)))



# 每件衣服的销售（件数）占比1
num1_dict = dict()
num_dict = dict()
clothes = ['羽绒服', '牛仔裤', '风衣', '皮草', 'T血', '马甲', '皮衣', '小西装', '卫衣', '衬衫', '休闲裤', '铅笔裤', '棉衣']
#
#
# def add_clot(num_clo):
#     for k in clothes:
#         if data1[num_clo] == k:
#             num_dict[data1[num_clo]] += data2[num_clo]


def sum_dict(a, b):

    temp = dict()
    for key in a.keys() | b.keys():
        temp[key] = sum(d.get(key, 0) for d in (a, b))
    return temp
# for i in st.keys():
#     data1 = st[i].col_values(1)
#     data2 = st[i].col_values(4)
#     data2.pop(0)
#     data1.pop(0)
#     data2 = list(map(int, data2))
#     num_dict = dict.fromkeys(data1, 0)
#     for j in range(len(data1)):
#         add_clot(j)
#
#     for key in num_dict:
#         percent = num_dict[key] / sum(num_dict.values())
#         print('%s的%s月销售占比为:%s' % (key, i, '%.2f%%' % (percent * 100)))  # 月销售占比
#     sum1 = sum_dict(num_dict, num1_dict)
#     num1_dict = sum1

# print(sum1)
# for key in sum1:
#     percent = sum1[key] / sum(sum1.values())
#     print('%s的年销售占比为:%s' % (key, '%.2f%%' % (percent * 100)))  # 年销售占比
number2_dict = dict()
number1_dict = dict()
number_dict = dict()
num3 = num4 = num5 = num6 =dict()
for i in st.keys():
    data3 = st[i].col_values(2)
    data1 = st[i].col_values(1)
    data2 = st[i].col_values(4)
    data3.pop(0)
    data1.pop(0)
    data2.pop(0)
    number1_dict = dict.fromkeys(data1, 0)
    for k in range(len(data1)):
        for j in clothes:
            if data1[k] == j:
                number1_dict[j] += data2[k]*data3[k]
    sum2 = sum_dict(number1_dict, number_dict)
    number_dict = sum2
    while True:
        if 2<= i <=4:
            number2_dict = dict.fromkeys(data1, 0)
            for k in range(len(data1)):
                for j in clothes:
                    if data1[k] == j:
                        number2_dict[j] += data2[k] * data3[k]
            num3 = sum_dict(number2_dict, number_dict)

            number_dict = num3
        if 5<= i <=7:
            number2_dict = dict.fromkeys(data1, 0)
            for k in range(len(data1)):
                for j in clothes:
                    if data1[k] == j:
                        number2_dict[j] += data2[k] * data3[k]
            num4 = sum_dict(number2_dict, number_dict)

            number_dict = num4
        if 8<= i <=10:
            number2_dict = dict.fromkeys(data1, 0)
            for k in range(len(data1)):
                for j in clothes:
                    if data1[k] == j:
                        number2_dict[j] += data2[k] * data3[k]
            num5 = sum_dict(number2_dict, number_dict)

            number_dict = num5
        if 11<= i <=12 or i == 1:
            number2_dict = dict.fromkeys(data1, 0)
            for k in range(len(data1)):
                for j in clothes:
                    if data1[k] == j:
                        number2_dict[j] += data2[k] * data3[k]
            num6 = sum_dict(number2_dict, number_dict)
            number_dict = num6

        break

for key, value in num3.items():
    if value == max(num3.values()):
        print('第一季最畅销的衣服：', key, '卖了：￥%.2f' % value)

for key, value in num4.items():
  if value == max(num4.values()):
     print('第二季最畅销的衣服：', key, '卖了：￥%.2f' % value)

for key, value in num5.items():
    if value == max(num5.values()):
        print('第三季最畅销的衣服：', key, '卖了：￥%.2f' % value)

for key, value in num6.items():
   if value == max(num6.values()):
      print('第四季最畅销的衣服：', key, '卖了：￥%.2f' % value)

for key in sum2:
    print('%s占全年销售额：' % key, '%.2f%%' % (sum2[key] / sum(sal1) * 100))

max(sum2.values())
for key, value in sum2.items():
    if value == max(sum2.values()):
        print('最畅销的衣服：', key, '卖了：￥%.2f' % value)


for key, value in sum2.items():
    if value == min(sum2.values()):
        print('畅销最低的衣服：', key, '卖了：￥%.2f' % value)









