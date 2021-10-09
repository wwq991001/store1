# 输入圆的半径计算计算周长和面积
import math

r = float(input('请输入圆的半径：'))
c = 2*r*math.pi
s = math.pi*math.pow(r, 2)
print("该圆的周长为", "{:.2f}".format(c))
print("该圆的面积为：", "{:.2f}".format(s))
