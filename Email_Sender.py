# coding:utf-8
# =========================================================================
# 加密SMTP
#
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
# =========================================================================
# from test import subinfo
from email.header import Header
# from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate
import smtplib
import configparser
# import io
# import sys

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

config = configparser.ConfigParser()
def emailsender(video_name, sub_url, episode_name):
    # =========================================================================
    # 设置参数
    # =========================================================================
    # 发送参数：发送地址
    config.read("myAccount.ini")

    from_addr = config.get("Email", 'sendEmail')
    # 接收参数: 客户端授权密
    password = config.get("Email", 'password')
    # 接收参数: 收件人地址,可多个
    to_addrs = [config.get("Email", 'receiveEmail1'),config.get("Email", 'receiveEmail2')]
    # 接收参数: SMTP服务器(注意:是发件人的smtp服务器)
    smtp_server = 'smtp.139.com'
    # 接收参数: 邮件主题
    subject = video_name+episode_name
    # 接收参数: 邮件正文
    video_name = video_name.replace(" ","+",-1)
    video_download_url = 'https://rarbg.to/torrents.php?search=%s+1080p' % video_name
    mail_msg = '<p><a href=%s' % sub_url + '>%s</a></p>' % sub_url + '\n' + \
               '<p><a href=%s' % video_download_url + '>%s</a></p>' % video_download_url



    def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr((Header(name, 'utf-8').encode(), addr))

    # 指定subtype为alternative，同时支持html和plain格式
    msg = MIMEMultipart('alternative')
    # 邮件正文中显示图片，同时附件的图片将不再显示
    msg.attach(MIMEText(str(mail_msg), 'html', 'utf-8'))       # 纯文本
    # 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
    msg['From'] = _format_addr(from_addr)
    # msg['To'] = _format_addr(to_addrs)
    msg['To'] = '%s' % ','.join([_format_addr('<%s>' % to_addr)
                                 for to_addr in to_addrs])
    msg['Subject'] = Header(str(subject), 'utf-8').encode()
    msg['Date'] = formatdate()
    # =========================================================================
    # 发送邮件
    # =========================================================================
    # SMTP服务器设置(地址,端口):
    server = smtplib.SMTP_SSL(smtp_server, 465)
    try:
        # SMTP服务器设置(地址,端口):
        # server = smtplib.SMTP_SSL(smtp_server, 465)
        # server.set_debuglevel(1)
        # 连接SMTP服务器(发件人地址, 客户端授权密码)
        server.login(from_addr, password)

        # 发送邮件
        server.sendmail(from_addr, to_addrs, msg.as_string())

        print('邮件发送成功', subject)
        print(sub_url)
        print(video_download_url)

    except smtplib.SMTPException as e:
        print(e)
        print('邮件发送失败')

    finally:
        # 退出SMTP服务器
        server.quit()

# emailsender('Agents of S.H.I.E.L.D.', 'http://subhd.com/zu0/14/d/27042712', '23')
