# -*- coding: utf-8 -*-

import configparser


# 读取配置文件
config = configparser.ConfigParser()
config.read("video_data.ini")

# Arrow http://subhd.com/zu/14/d/26749162
try:
    config.add_section("Arrow")
    config.set("Arrow", "url", "http://subhd.com/zu/14/d/26749162")
    config.set("Arrow", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'Arrow' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


# Gotham  http://subhd.com/zu/14/d/26752161
try:
    config.add_section("Gotham")
    config.set("Gotham", "url", "http://subhd.com/zu/14/d/26752161")
    config.set("Gotham", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'Gotham' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


# Blindspot  http://subhd.com/zu/14/d/26661659
try:
    config.add_section("Blindspot")
    config.set("Blindspot", "url", "http://subhd.com/zu/14/d/26661659")
    config.set("Blindspot", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'Blindspot' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


# The Flash  http://subhd.com/zu/14/d/26749151
try:
    config.add_section("The Flash")
    config.set("The Flash", "url", "http://subhd.com/zu/14/d/26749151")
    config.set("The Flash", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'The Flash' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


# The Vampire Diaries  http://subhd.com/zu/14/d/26749102
try:
    config.add_section("The Vampire Diaries")
    config.set("The Vampire Diaries", "url", "http://subhd.com/zu/14/d/26749102")
    config.set("The Vampire Diaries", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'The Vampire Diaries' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


# Supergirl  http://subhd.com/zu/14/d/26792305
try:
    config.add_section("Supergirl")
    config.set("Supergirl", "url", "http://subhd.com/zu/14/d/26792305")
    config.set("Supergirl", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'Supergirl' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


# Sleepy Hollow http://subhd.com/zu/14/d/26793081
try:
    config.add_section("Sleepy Hollow")
    config.set("Sleepy Hollow", "url", "http://subhd.com/zu/14/d/26793081")
    config.set("Sleepy Hollow", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'Sleepy Hollow' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


# Agents of S.H.I.E.L.D.  http://subhd.com/zu/14/d/26740391
try:
    config.add_section("Agents of S.H.I.E.L.D.")
    config.set("Agents of S.H.I.E.L.D.", "url", "http://subhd.com/zu/14/d/26740391")
    config.set("Agents of S.H.I.E.L.D.", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'Agents of S.H.I.E.L.D.' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


# Legends of Tomorrow   http://subhd.com/zu/14/d/26749014
try:
    config.add_section("Legends of Tomorrow")
    config.set("Legends of Tomorrow", "url", "http://subhd.com/zu/14/d/26749014")
    config.set("Legends of Tomorrow", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'Legends of Tomorrow' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))

# Lucifer   http://subhd.com/do0/26974949
try:
    config.add_section("Lucifer")
    config.set("Lucifer", "url", "http://subhd.com/do0/26974949")
    config.set("Lucifer", "episode", '1')
except configparser.DuplicateSectionError:
    print("Section 'Lucifer' already exists")
# 写入配置文件
config.write(open("video_data.ini", "w"))


#
# ip = config.get("School", "IP")
# mask = config.get("School", "mask")
# gateway = config.get("School", "Gateway")
# dns = config.get("School", "DNS")
# print(config.get("Arrow", "episode"))
# from Email_Sender import emailsender
# emailsender()
