# 华氏温度转换为摄氏温度
while True:
    fahrenheit = input("请输入华氏温度(输入q/Q结束)：℉")
    if fahrenheit == 'q' or fahrenheit == 'Q':
        break
    celsius = (float(fahrenheit) - 32) / 1.8
    print('摄氏温度为：℃', "{:.2f}".format(celsius))

