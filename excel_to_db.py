import pymysql
import xlrd

host = "localhost"
user = "root"
password = "root"
port = 3306
# db = "2020年每个月的销售情况"
conn = pymysql.connect(host=host, user=user, password=password, port=port)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE 2020年每个月的销售情况 CHARACTER SET utf8;")
cursor.execute("use 2020年每个月的销售情况")
wb = xlrd.open_workbook(filename='E:\\PYthon自动化测试\\python\\python任务\\day7\\任务\\2020年每个月的销售情况.xlsx',
                        encoding_override=True)
df = wb.sheet_names()

for j in range(len(df)):
    sql = "create table %s月(日期 char(4) , " \
          "服装名称 char(8)," \
          "价格件 double(6,1), " \
          "本月库存数量 int, " \
          "销售量每日 int);"
    param = [j+1]
    cursor.execute(sql, param)

for i in range(len(df)):
    st = wb.sheet_by_index(i)
    nrow = st.nrows
    ncol = st.ncols
    sql = "insert into %s月(日期,服装名称,价格件,本月库存数量,销售量每日) values(%s,%s,%s,%s,%s)"
    for k in range(1, nrow):
        param = [i + 1]
        for m in range(ncol):
            param.append(st.cell(k, m).value)
        print(param)
        cursor.execute(sql, param)
    columns = str(st.ncols)
    rows = str(nrow)
    print("导入"+columns+"列"+rows+"行到数据库")

conn.commit()
cursor.close()
conn.close()

