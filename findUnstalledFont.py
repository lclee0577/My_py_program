# -*- encoding:UTF-8 -*-
"""
This is a test for find the font in ass file
"""
import re
import time
import io
import sys
import os
import webbrowser

import wx
from wx import FontEnumerator

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

print(time.ctime())

installed_fonts = ['FZZhunYuan-M02',  'Microsoft YaHei'
                   ]

# installed_fonts = ['微软雅黑', '方正综艺简体', '方正隶变简体', '方正小标宋简体', \
#                     '方正卡通简体', '方正粗圆简体', '方正粗宋简体', '方正大黑简体',\
#                     '方正超粗黑简体','方正华隶简体','华文中宋','宋体','德彪钢笔行书字库',\
#                     '方正粗宋_GBK','方正楷体简体','方正静蕾简体','方正大标宋简体','方正超粗黑_GBK',\
#       '方正艺黑简体','方正兰亭特黑简体','方正兰亭特黑长简体','迷你霹雳体'
#       ]

aaa = wx.App(False)
My_fonts1 = wx.FontEnumerator().GetFacenames()


length = len(My_fonts1)
for i in range(length):
    if i < length:
        if '@' in My_fonts1[i]:
            My_fonts1.remove(My_fonts1[i])
            length = len(My_fonts1)

with open("Fontdict.txt", 'a',encoding="utf-8") as f:
    # f.seek(0, 0)
    for i in range(len(My_fonts1)):
        f.write(str(My_fonts1[i])+'\n')

My_fonts2 = os.listdir('C:\\Windows\\Fonts')
for i in range(len(My_fonts2)):
    if '.' in My_fonts2[i]:
        sub_s = My_fonts2[i].find('.')
        My_fonts2[i] = My_fonts2[i][:sub_s]

with open("Fontdict.txt", 'a',encoding="utf-8") as f:
    # f.seek(0, 0)
    for i in range(len(My_fonts2)):
        f.write(str(My_fonts2[i])+'\n')

My_fonts1.extend(My_fonts2)
My_fonts = list(set(My_fonts1))
My_fonts.extend(installed_fonts)

# with open("Fontdict.txt", 'a',encoding="utf-8") as f:
#     # f.seek(0, 0)
#     for i in range(len(My_fonts)):
#         f.write(str(My_fonts[i])+'\n')

# print(My_fonts)
# print(os.getcwd())

assFileName = os.listdir(os.getcwd())
length = len(assFileName)
i = 0
while (i < length):
    if i < length:
        if 'ass' not in assFileName[i]:
            assFileName.remove(assFileName[i])
            i -= 1
            length = len(assFileName)
    i += 1


def readAssFile(Name, encodestyle):
        with open(Name, 'r+', encoding=encodestyle) as f:
            txt = f.read()
            fontName = re.findall('fn(.*?)}', txt)
            styleFont = re.findall('Style: (.*?),(.*?),', txt)
            for i in range(len(styleFont)):
                fontName.append(styleFont[i][1])

            fontName = list(set(fontName))
            for i in range(len(fontName)):
                if '\\' in fontName[i]:
                    sub_s = fontName[i].find('\\')
                    fontName[i] = fontName[i][:sub_s]
            fontName = list(set(fontName))

            if 'FZLanTingHei-R-GBK' in txt:
                txt1 = txt.replace("FZLanTingHei-R-GBK", "方正黑体_GBK")
                print('replace FZLanTingHei with 方正黑体_GBK')
                f.seek(0, 0)
                f.write(txt1)

            for i in range(len(fontName)):
                if fontName[i] in My_fonts:
                    print('find', fontName[i])
                else:
                    print('not find', fontName[i])
                    webbrowser.open(
                        "https://www.baidu.com/s?wd=" + fontName[i])
            print("\n")


def findFont(fileName):
        try:
            readAssFile(fileName, 'utf-8-sig')

        except UnicodeDecodeError:
            readAssFile(fileName, 'utf-16')


for i in range(len(assFileName)):
    print(assFileName[i])
    findFont(assFileName[i])

a = input("press enter to exit")
# print(fontName)
