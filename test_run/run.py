import os
import sys
import time
import logging
import unittest
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from HTMLTestRunnerCN import HTMLTestRunner
from email.mime.multipart import MIMEMultipart


# 发送邮箱
def sen_email_html(file_dir):
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'

    # 发送邮箱用户和密码
    user = '17620016080@163.com'
    password = 'Che123456n'

    # 发送和接收邮箱
    sender = '17620016080@163.com'
    receives = ['2675046489@qq.com', '17620016080@163.com']

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    # 发送邮件主题和内容
    subject = '将军财富'+now+'自动化测试报告'
    content = '<html><hl style="color:red">自动化测试报告</hl></html>'

    # 构造附件内容
    send_file = open(file_dir, 'rb').read()

    # HTML邮件正文
    att = MIMEText(send_file, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    # 附件信息
    msg = MIMEMultipart()
    msg.attach(MIMEText(content, 'html', 'utf-8'))
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives) # 以,为标准进行分割加入到接收者邮箱中
    msg.attach(att)
    # 登录并发送邮件
    try:
        # SSL协议端口号要使用
        smtp = smtplib.SMTP_SSL(smtpserver, 465)

        # 向服务器标识用户身份
        smtp.helo(smtpserver)

        # 服务器返回结果确认
        smtp.ehlo(smtpserver)

        # 登录服务器用户和明码
        smtp.login(user, password)
        print('开始发送邮箱……')
        smtp.sendmail(sender, receives, msg.as_string())
    except smtplib.SMTPException as e:
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        smtp.quit()


# 查找目录下最新的文件
def find_new_file(file_dir):
    file_lists = os.listdir(file_dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(file_dir + "\\" + fn)
                    if not os.path.isdir(file_dir + "\\" + fn)
                    else 0)
    # print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(file_dir, file_lists[-1])
    return file


# 加载项目的根目录
path = 'D:\\kyb_testProject\\'
sys.path.append(path)

# 指定测试用例和测试报告路径
test_dir = '../test_cast'
report_dir = '../reports'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')# 更多的test用例可以使用test*.py

# 定义报告的文件格式
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+'test_report.html'

# 运行测试用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='自动化测试报告',
                            description='详细测试用例结果',
                            tester='CWJ')  # tester 测试人员姓名
    logging.info('------start run testcase------')
    runner.run(discover)
report_dir = '../reports'  # 指定文件目录
file_dir = find_new_file(report_dir)  # 查找最新的html文件
sen_email_html(file_dir)