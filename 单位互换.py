# 英制单位英寸与公制单位厘米互换

while True:
    judge = int(input("您要输入英寸还是厘米？1：英寸,2：厘米,3：退出:"))
    if judge == 1:
        inch = float(input("请输入英寸(in)："))
        mil = inch * 2.54
        print('厘米为：', mil, 'cm')
    if judge == 2:
        mil = float(input("请输入厘米(cm)："))
        inch = mil / 2.54
        print('英寸为：', "{:.2f}".format(inch), 'in')
    if judge == 3:
        print("下次再见！")
        break

