# 输入三条边长，如果能构成三角形就计算周长和面积

a = []
for i in range(3):
    a.append(float(input("请输入三角形边长：")))
if a[0] + a[1] > a[2] and a[0] + a[2] > a[1] and a[1] + a[2] > a[0]:
    c = sum(a)
    p = c / 2
    s = pow(p * (p - a[0]) * (p - a[1]) * (p - a[2]), 0.5)
    print("可以构成三角形")
    print("该三角形周长为：", c)
    print('该三角形面积为：', "{:.2f}".format(s))
else:
    print("不能构成三角形！")
