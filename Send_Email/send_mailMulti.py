import smtplib      # 发送邮箱模块
from email.mime.text import MIMEText    # 定义邮箱内容
from email.header import Header # 定义邮箱标题
from email.mime.multipart import MIMEMultipart # 定义附件内容

# 发送邮箱服务器
smtpserver = 'smtp.163.com'

# 发送邮箱用户和密码
user = '17620016080@163.com'
password = 'Che123456n'

# 发送和接收邮箱
sender = '17620016080@163.com'
receives = ['2675046489@qq.com', '17620016080@163.com']

# 发送邮件主题和内容
subject = '将军财富APP'
content = '<html><hl style="color:red">我要自学网</hl></html>'

# 构造附件内容
send_file = open(r'D:\download\python.png', 'rb').read()

# HTML邮件正文
att = MIMEText(send_file, 'base64', 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="python.png"'
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