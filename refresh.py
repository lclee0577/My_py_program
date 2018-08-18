#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from Email_Sender import emailsender
# emailsender() 输入（美剧名称，网址）便可发送到邮箱
# 例如 emailsender('Arrow', 'http://subhd.com/d/26749162')
# emailsender('Arrow', 'http://subhd.com/d/26749162\nhttps://rarbg.to/torrents.php?search=Arrow+1080p')
# website = 'http://subhd.com/d/26749162\nhttps://rarbg.to/torrents.php?search=Arrow+1080p'
# print(website)

import urllib.request

# 定义保存函数


def save_file(data):
    path = "D:\\My_py_program\\website_data.out"
    f = open(path, 'wb')
    f.write(data)
    f.close()


# 打印抓取的内容
# print(data)
# episode = 10
# episode_name = '第 %s 集' %episode


def find_string(date, episode_name):
    try:
        str.index(date, episode_name)
        return 'find'
    except (ValueError):
        return 'not find'


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
        save_file(data)
        data = data.decode('utf-8')
        episode_name = '第 %s 集' % episode
        result = find_string(data, episode_name)
        return result
    except TimeoutError:
        result = 'not find'
    except UnboundLocalError:
        result = 'not find'
    except urllib.error.URLError:
        result = 'not find'
    finally:
         return result

# print(refresh('http://subhd.com/zu/14/d/26749162', '8'))

# 打印爬取网页的各类信息
# print(type(res))
# print(res.geturl())
# print(res.info())
# print(res.getcode())
