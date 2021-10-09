# 百分制成绩转换为等级制成绩

results = float(input("请填写成绩(0-100)："))

if 90 <= results <= 100:
    print("该成绩评为A")
elif 80 <= results < 90:
    print("该成绩评为B")
elif 70 <= results < 80:
    print("该成绩评为C")
elif 60 <= results < 70:
    print("该成绩评为D")
elif 0 <= results < 60:
    print("该成绩评为E")
else:
    print("请不要乱填写！")
