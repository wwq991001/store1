


f = open(r'E:\PYthon自动化测试\python\python任务\day15【异常处理】\baidu_x_system.log','r',encoding='utf-8')
data = f.readlines()
a = list()
b = dict()
for i in data:
    c = ""
    # a.append(i[0:13])
    for j in i:
        if j.isspace():
            break
        else:
            c += j
    a.append(c)


for j in a:
    b[j] = a.count(j)
print(b)












