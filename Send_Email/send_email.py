import smtplib      # 发送邮箱模块
from email.mime.text import MIMEText    # 定义邮箱内容
from email.header import Header # 定义邮箱标题

# 发送邮箱服务器
smtpserver = 'smtp.163.com'

# 发送邮箱用户和密码
user = '17620016080@163.com'
password = 'Che123456n'

# 发送和接收邮箱
sender = '17620016080@163.com'
receive = '2675046489@qq.com'

# 发送邮件主题和内容
subject = '将军财富APP'
content = '<html><hl style="color:red">我要自学网</hl></html>'

# HTML邮件正文
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender
msg['To'] = receive

# SSL协议端口号要使用
smtp = smtplib.SMTP_SSL(smtpserver, 465)

# 向服务器标识用户身份
smtp.helo(smtpserver)
# 服务器返回结果确认
smtp.ehlo(smtpserver)
# 登录服务器用户和明码
smtp.login(user, password)

print('开始发送邮箱……')
smtp.sendmail(sender, receive, msg.as_string())
smtp.quit()
print('邮件发送完成！')