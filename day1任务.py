import xlrd
import numpy as np

d = xlrd.open_workbook("12月份衣服销售数据.xlsx", encoding_override=True)
d_s = d.sheet_by_index(0)
rows = d_s.nrows
cols = d_s.ncols
a = []
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
x = [c,d,e,f,g,h]
clo_name = ["羽绒服", "牛仔裤", "风衣", "皮草", "T血", "衬衫"]
percent = [0,1,2,3,4,5]

for i in range(rows):
    data = d_s.row_values(i)
    print(data)

for i in range(1, rows):
    data = d_s.row_values(i)
    a.append(data[2] * data[4])
    for j in range(6):
        if data[1] == clo_name[j]:
            x[j] += data[4]


b = d_s.col_values(4)
b.remove(b[0])
avg = np.mean(b)


print('本月销售总额：￥', "{:.1f}".format(sum(a)))
print('本月平均销售量', int(avg), '件')
for i in range(6):
    percent[i] = x[i] / sum(b)
    print('本月', clo_name[i], '销售占比', '%.2f%%' % (percent[i] * 100))
