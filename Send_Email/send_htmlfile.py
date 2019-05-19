# 发送html内容的邮件
import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header


def send_mail_html(file):
    '''发送html内容邮件'''
    # 发送邮箱
    sender = '17620016080@163.com'
    # 接收邮箱
    receiver = '17620016080@163.com'
    # 发送邮件主题
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    subject = '自动化测试结果_' + t
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户/密码
    username = '17620016080@163.com'
    password = 'Che123456n'

    # 读取html文件内容
    f = open(file, 'rb').read()
    mail_body = '自动化测试报告附件'

    # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    # 登录并发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
    except:
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        smtp.quit()


def find_new_file(dir):
    '''查找目录下最新的文件'''
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
                    if not os.path.isdir(dir + "\\" + fn)
                    else 0)
    # print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(dir, file_lists[-1])
    print('完整文件路径：', file)
    return file


report_dir = '../reports'  # 指定文件目录
file = find_new_file(report_dir)  # 查找最新的html文件
send_mail_html(file)# 发送html内容邮件
