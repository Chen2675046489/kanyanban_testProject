import os
import time
import smtplib      # 发送邮箱模块
from email.mime.text import MIMEText    # 定义邮箱内容
from email.header import Header # 定义邮箱标题
from email.mime.multipart import MIMEMultipart # 定义附件内容


# 发送邮箱
def sen_email_html():
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
    report_dir = '../reports'
    file = find_new_file(report_dir)
    send_file = open(file, 'rb').read()

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
    smtp.quit()
    print('邮件发送完成！')


# 查找目录下最新的文件
def find_new_file(file_dir):
    file_lists = os.listdir(file_dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(file_dir + "\\" + fn)
                    if not os.path.isdir(file_dir + "\\" + fn)
                    else 0)
    # print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(file_dir, file_lists[-1])
    print('完整文件路径：', file)
    return file