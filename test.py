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
i = 0
while 1:

    config.read("video_data.ini")
   
    print(time.ctime(), '\n')  
    # Arrow
    result = str(refresh(config.get("Arrow", 'url'), config.get("Arrow", 'episode')))
    if result == 'find':
        episode = config.get("Arrow", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Arrow', config.get("Arrow", 'url'), episode_name)
        config.set("Arrow", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find Arrow \n")

    # Gotham
    result = str(refresh(config.get("Gotham", 'url'), config.get("Gotham", 'episode')))
    if result == 'find':
        episode = config.get("Gotham", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Gotham', config.get("Gotham", 'url'), episode_name)
        config.set("Gotham", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find Gotham \n")        

    # Blindspot
    result = str(refresh(config.get("Blindspot", 'url'), config.get("Blindspot", 'episode')))
    if result == 'find':
        episode = config.get("Blindspot", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Blindspot', config.get("Blindspot", 'url'), episode_name)
        config.set("Blindspot", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find Blindspot \n")

    # The Flash
    result = str(refresh(config.get("The Flash", 'url'), config.get("The Flash", 'episode')))
    if result == 'find':
        episode = config.get("The Flash", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('The Flash', config.get("The Flash", 'url'), episode_name)
        config.set("The Flash", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find The Flash \n")

    # Supergirl
    result = str(refresh(config.get("Supergirl", 'url'), config.get("Supergirl", 'episode')))
    if result == 'find':
        episode = config.get("Supergirl", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Supergirl', config.get("Supergirl", 'url'), episode_name)
        config.set("Supergirl", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find Supergirl \n")
    # # Sleepy Hollow
    # result = str(refresh(config.get("Sleepy Hollow", 'url'), config.get("Sleepy Hollow", 'episode')))
    # if result == 'find':
    #     episode = config.get("Sleepy Hollow", "episode")
    #     episode_name = ' 第 %s 集' % episode
    #     emailsender('Sleepy Hollow', config.get("Sleepy Hollow", 'url'), episode_name)
    #     config.set("Sleepy Hollow", "episode", '%s' % (str(int(episode) + 1)))
    #     config.write(open("video_data.ini", "w"))
    #     print(time.ctime(), '\n')

    # Agents of S.H.I.E.L.D.
    result = str(refresh(config.get("Agents of S.H.I.E.L.D.", 'url'), config.get("Agents of S.H.I.E.L.D.", 'episode')))
    if result == 'find':
        episode = config.get("Agents of S.H.I.E.L.D.", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Agents of S.H.I.E.L.D.', config.get("Agents of S.H.I.E.L.D.", 'url'), episode_name)
        config.set("Agents of S.H.I.E.L.D.", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find Agents of S.H.I.E.L.D. \n")

    # Legends of Tomorrow
    result = str(refresh(config.get("Legends of Tomorrow", 'url'), config.get("Legends of Tomorrow", 'episode')))
    if result == 'find':
        episode = config.get("Legends of Tomorrow", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Legends of Tomorrow', config.get("Legends of Tomorrow", 'url'), episode_name)
        config.set("Legends of Tomorrow", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find Legends of Tomorrow \n")

    # The Originals
    result = str(refresh(config.get("The Originals", 'url'), config.get("The Originals", 'episode')))
    if result == 'find':
        episode = config.get("The Originals", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('The Originals', config.get("The Originals", 'url'), episode_name)
        config.set("The Originals", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find The Originals \n")

    # Legion
    result = str(refresh(config.get("Legion", 'url'), config.get("Legion", 'episode')))
    if result == 'find':
        episode = config.get("Legion", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Legion', config.get("Legion", 'url'), episode_name)
        config.set("Legion", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')
    else:
        print("not find Legion \n")

    # Lucifer
    result = str(refresh(config.get("Lucifer", 'url'), config.get("Lucifer", 'episode')))
    if result == 'find':
        episode = config.get("Lucifer", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Lucifer', config.get("Lucifer", 'url'), episode_name)
        config.set("Lucifer", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')   
    else:
        print("not find Lucifer \n")
 

    # The Gifted 
    result = str(refresh(config.get("The Gifted", 'url'), config.get("The Gifted", 'episode')))
    if result == 'find':
        episode = config.get("The Gifted", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('The Gifted', config.get("The Gifted", 'url'), episode_name)
        config.set("The Gifted", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n')          
    else:
        print("not find The Gifted  \n")
    # Counterpart  Counterpart
    result = str(refresh(config.get("Counterpart", 'url'), config.get("Counterpart", 'episode')))
    if result == 'find':
        episode = config.get("Counterpart", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Counterpart', config.get("Counterpart", 'url'), episode_name)
        config.set("Counterpart", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n') 
    else:
        print("not find Counterpart  \n")

    # Krypton
    result = str(refresh(config.get("Krypton", 'url'), config.get("Krypton", 'episode')))
    if result == 'find':
        episode = config.get("Krypton", "episode")
        episode_name = ' 第 %s 集' % episode
        emailsender('Krypton', config.get("Krypton", 'url'), episode_name)
        config.set("Krypton", "episode", '%s' % (str(int(episode) + 1)))
        config.write(open("video_data.ini", "w"))
        print(time.ctime(), '\n') 
    else:
        print("not find Krypton  \n")
              
    print(time.ctime(), '\n')  

    i += 1   
    print(i)
    # time.sleep(10)
    if (i == 2):
        a = input("press enter to continue, 0 to exit     ")
        
    
        