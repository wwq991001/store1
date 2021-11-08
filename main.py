'''
    1.加载所有的测试用例
    2.执行用例并生成测试报告
'''
from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from mail1 import send_mail

# 1.加载所有用例
address = r"E:\PYthon自动化测试\python\python任务\day13【单元测试】\代码\day13"
tests = unittest.defaultTestLoader.discover(address, pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器的测试报告",
    description="这是综合测试报告",
    verbosity=1,
    stream=open(file="计算器.html", mode="w+", encoding="utf-8")
)

# 3.执行用例
runner.run(tests)

# 4.任务： 使用邮件发送附件，把报告发送给我
sender = "1942936605@qq.com"
passwd = "xlklojkmgdwlfbfe"
receivers = "wwq991001@outlook.com"

subject = "计算器的综合测试报告"
content = address + '\\计算器.html'
f = open(content, 'rb')
mail_body = f.read()
f.close()

msg = MIMEText(mail_body, "html", 'utf-8')
msg['Subject'] = Header(subject, "utf-8")
msg['From'] = sender
msg['TO'] = receivers

try:
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.login(sender, passwd)
    s.sendmail(sender, receivers, msg.as_string())
    print("发送成功")

except smtplib.SMTPException as e:
    print("发送失败,失败原因", e)

# send_address = "1942936605@qq.com"
# send_password = 'xlklojkmgdwlfbfe'
# receive_address = "wwq991001@outlook.com"
# title = "计算器的综合测试报告"
# content = "Hi，你好！这封邮件是python发送的"
# attachfilepath = "计算器.html"
# send_mail(send_address,send_password,receive_address,title,content,file=attachfilepath)
# print("成功")


