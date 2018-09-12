
# -*- coding: utf-8 -*-
# from Email_Sender import emailsender
# emailsender() 输入（美剧名称，网址）便可发送到邮箱
# 例如 emailsender('Arrow', 'http://subhd.com/d/26749162')
# emailsender('Arrow', 'http://subhd.com/d/26749162\nhttps://rarbg.to/torrents.php?search=Arrow+1080p')
# website = 'http://subhd.com/d/26749162\nhttps://rarbg.to/torrents.php?search=Arrow+1080p'
# print(website)#000000

import urllib.request
import re
import webbrowser
import sys
import io
import time
import configparser

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 定义保存函数


def save_file(data):
    path = "/home/lclee/website_data.html"
    f = open(path, 'wb')
    f.write(data)
    f.close()


# 打印抓取的内容
# print(data)
# episode = 10
# episode_name = '第 %s 集' %episode


def find_string(date, episode):
    episode_name = '第 %s 集' % episode
    #print(episode_name)
    try:
        str.index(date, episode_name)
        # 寻找是否有最新一集的字幕更新，没有则抛出异常
        subBegin = date.find(episode_name)
        subEnd = date.find('第 %d 集' % (int(episode)-1))
        date = date[subBegin:subEnd]
        # 选取最新一集的字幕列表
        beninStr = '<a href='
        stopStr = '</a></div>'
        names = re.findall('%s.*?%s' % (beninStr, stopStr), date)
        for i in range(len(names)):
            # 删除起始和结束的标志
            if "1080p" in names[i]:
                url = "http://subhd.com" + re.sub(r'%s|class.*%s|\"' % (beninStr, stopStr), '', names[i])
                names[i] = re.sub(r'%s.*?>|%s' % (beninStr, stopStr), '', names[i])
                # webbrowser.open(url)
                # print("http://subhd.com"+url)
                print(names[i])
                return 'find'
        return 'not find'
    except (ValueError):
        return 'not find'
        print("ValueError")


# result = find_string(data, episode_name)
# print(result)


def refresh(url, episode):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }

    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    # Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393
    try:
        req = urllib.request.Request(url=url, headers=headers)

        res = urllib.request.urlopen(req)

        data = res.read()
        # save_file(data)
        data = data.decode('utf-8')
        result = find_string(data, episode)
        return result
    except TimeoutError:
        result = 'not find'
        print("TimeoutError")
    except UnboundLocalError:
        result = 'not find'
        print("UnboundLocalError")
    except urllib.error.URLError:
        result = 'not find'
        print("urllib.error.URLError")
    finally:
        return result




# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
# =========================================================================
# from test import subinfo
from email.header import Header
# from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate
import smtplib

config1 = configparser.ConfigParser()
def emailsender(video_name, sub_url, episode_name):
    # =========================================================================
    # 设置参数
    # =========================================================================
    # 发送参数：发送地址
    config1.read("myAccount.ini")

    from_addr = config1.get("Email", 'sendEmail')
    # 接收参数: 客户端授权密
    password = config1.get("Email", 'password')
    # 接收参数: 收件人地址,可多个
    to_addrs = [config1.get("Email", 'receiveEmail1'),config1.get("Email", 'receiveEmail2')]
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

    except TimeoutError as e:
        print(e)
        print('邮件发送失败')

    except WinError as e:
        print(e)
        print('邮件发送失败')
        
    finally:
        # 退出SMTP服务器
        server.quit()


config = configparser.ConfigParser()
config.read("video_data.ini")
name = config.sections()
loopcount = 0
exitFlag = 1
daycount = 0
sleeptime = 5
dayFlag = 24*60*60/sleeptime
while exitFlag == 1:

    config.read("video_data.ini")
   
    print(time.ctime(), '\n')  
    

    name = config.sections()
    i = 0
    for i in range(len(name)):
        episode = config.get(name[i], "episode")
        url = config.get(name[i], 'url')
        result = str(refresh(url, episode))
        if result == 'find':
            episode_name = ' 第 %s 集 from Ubuntu' % episode
            emailsender(name[i], url, episode_name)
            config.set(name[i], "episode", '%s' % (str(int(episode) + 1)))
            config.write(open("video_data.ini", "w"))
            #webbrowser.open(url)
            #webbrowser.open('https://rarbg.to/torrents.php?search=%s+1080p' % name[i])
            print(time.ctime())
        else:
            print("not find %s \n" % name[i])

    loopcount += 1
    time.sleep(sleeptime)
    if loopcount >= dayFlag:
         loopcount = 0
         daycount +=1
         emailsender("Ubuntu have been work", "already run %d days" %daycount, " %d days" %daycount)
    
         #exitFlag = input("press enter to continue, 0 to exit     ")

