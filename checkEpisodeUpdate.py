# coding:utf-8
import configparser
import time
from refresh import refresh
from Email_Sender import emailsender
import os
import io
import sys




# 读取配置文件
config = configparser.ConfigParser()
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# config.read("video_data.ini")
# print(config.get("Arrow",'url'))
# print(refresh(config.get("Arrow",'url'),config.get("Arrow",'episode')))
# print(time.ctime(), '\n')  
loopcount = 0
exitFlag = 1
while exitFlag == 1:

    config.read("video_data.ini")
   
    print(time.ctime(), '\n')  
    

    name = config.sections()
    i = 0
    for i in range(len(name)):
        result = str(refresh(config.get(name[i], 'url'), config.get(name[i], 'episode')))
        if result == 'find':
            episode = config.get(name[i], "episode")
            episode_name = ' 第 %s 集' % episode
            emailsender(name[i], config.get(name[i], 'url'), episode_name)
            config.set(name[i], "episode", '%s' % (str(int(episode) + 1)))
            config.write(open("video_data.ini", "w"))
            print(time.ctime(), '\n')
        else:
            print("not find %s \n" %name[i])

    loopcount += 1

    if loopcount == 2:
         exitFlag = input("press enter to continue, 0 to exit     ")
        
             
    
   
   
        
    
        