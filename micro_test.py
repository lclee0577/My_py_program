#-*- encoding:UTF-8 -*-
# coding:utf-8
import configparser
import webbrowser




# 读取配置文件
config = configparser.ConfigParser()


config.read("video_data.ini")
name = config.sections()
print(name)
print(len(name))

for i in range(len(name)):
    print(name[i])
    webbrowser.open("https://www.baidu.com/s?wd="+name[i])
