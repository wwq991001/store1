# 输入年份判断是不是闰年

while True:
    year = input("请输入年份(输入q/Q退出)：")
    if year == 'q' or year == 'Q':
        break
    elif int(year) % 4 == 0:
        print(year, '年是闰年')
    elif int(year) % 4 != 0:
        print(year, "不是闰年")
    else:
        continue
