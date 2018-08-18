#-*- encoding:UTF-8 -*-
# coding:utf-8
import configparser




# 读取配置文件
config = configparser.ConfigParser()


config.read("video_data.ini")
name = config.sections()
print(name)
print(len(name))

for i in range(len(name)):
    print(name[i])