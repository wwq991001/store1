import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='company')
cursor = conn.cursor()
cursor.execute("use company;")


def add_fet(num):
    cursor.execute(num)
    for row in cursor.fetchall():
        print(row)
    print(cursor.rowcount, "record inserted")


# 1. 查询出部门编号为30的所有员工
cursor.execute("select * from t_employees  where deptno = 30")
results = cursor.fetchall()
print("编号   姓名   工作   上级领导   入职日期  薪资   奖金  部门编号")
for row in results:
    print(row)
print(cursor.rowcount, 'record inserted')

# 2. 所有经理的姓名、编号和部门编号。
a = "select ename, empno, deptno from t_employees where job = '经理'"
cursor.execute(a)
print("姓名   编号   部门编号")
for row in cursor.fetchall():
    print(row)
print(cursor.rowcount, 'record inserted')

# 3. 找出奖金高于工资的员工。
b = "select * from t_employees where comm > sal"
cursor.execute(b)
print("编号   姓名   工作   上级领导   入职日期  薪资   奖金  部门编号")
for row in cursor.fetchall():
    print(row)
print(cursor.rowcount, "record inserted")

# 4. 找出奖金高于工资60%的员工。
c = "select * from t_employees where comm > sal * 0.6"
cursor.execute(c)
print("编号   姓名   工作   上级领导   入职日期  薪资   奖金  部门编号")
for row in cursor.fetchall():
    print(row)
print(cursor.rowcount, "record inserted")

# 5. 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。
d = "select * from t_employees where (deptno = 10 and job = '经理') or (deptno = 20 and job = '分析员')"
cursor.execute(d)
print("姓名 编号   姓名   工作   上级领导   入职日期  薪资   奖金  部门编号")
for row in cursor.fetchall():
    print(row)
print(cursor.rowcount, "record inserted")

# 6.找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
e = "select * from t_employees where (deptno =10 and job = '经理') or (deptno = 20 and job = '分析员')" \
    "or (job != '经理' and job != '武装上将' and sal >= 3000)"
print("姓名 编号   姓名   工作   上级领导   入职日期  薪资   奖金  部门编号")
add_fet(e)

# 7.无奖金或奖金低于1000的员工。
f = "select ename, comm from t_employees where comm is null or comm <= 1000"
print("姓名   奖金")
add_fet(f)

# 8. 查询名字由三个字组成的员工。
g = "select ename from t_employees where ename like '___'"
print("姓名")
add_fet(g)

# 9. 查询2000年以及以后入职的员工。
h = "select ename, hiredate from t_employees where hiredate >= '2000-01-01'"
print("姓名")
add_fet(h)

# 10. 查询所有员工详细信息，用编号升序排序
m = "select * from t_employees order by empno asc"
print("姓名 编号   姓名   工作   上级领导   入职日期  薪资   奖金  部门编号")
add_fet(m)

# 11. 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
n = "select * from t_employees order by sal desc, hiredate asc"
print("姓名 编号   姓名   工作   上级领导   入职日期  薪资   奖金  部门编号")
add_fet(n)

# 12. 查询每个部门的平均工资
o = "select t.deptno, t1.dname, avg(t.sal) from t_employees t join t_dept t1 on t.deptno = t1.deptno group by t.deptno"
print("部门编号    部门    平均工资")
add_fet(o)

# 13. 查询每个部门的雇员数量。
p = "select t.deptno, t1.dname, count(ename) from t_employees t join t_dept t1 on t.deptno = t1.deptno group by deptno"
print("部门编号   部门    人员数量")
add_fet(p)

# 14. 查询每种工作的最高工资、最低工资、人数
q = "select job, max(sal), min(sal),count(ename) from t_employees group by job"
print("   工作   最高工资   最低工资   人数")
add_fet(q)
conn.commit()
