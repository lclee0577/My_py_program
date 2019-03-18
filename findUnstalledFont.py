
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


installed_fonts = ['FZZhunYuan-M02',  'Microsoft YaHei', "FZHei-B01", "FZZongYi-M05S", "cronos Pro Subhead",
                   "FZYiHei-M20", "FZLanTingHei-R-GBK", "方正黑体_GBK Light", "icomoon"
                   ]


def refreshFontList():
    aaa = wx.App(False)
    My_fonts1 = wx.FontEnumerator().GetFacenames()

    for i in range(len(My_fonts1)-1,-1,-1):
            if '@' in My_fonts1[i]:
                My_fonts1.remove(My_fonts1[i])

    My_fonts2 = os.listdir('C:\\Windows\\Fonts')
    for i in range(len(My_fonts2)):
        if '.' in My_fonts2[i]:
            sub_s = My_fonts2[i].find('.')
            My_fonts2[i] = My_fonts2[i][:sub_s]

    My_fonts1.extend(My_fonts2)
    My_fonts = list(set(My_fonts1))
    My_fonts.extend(installed_fonts)

    with open("Fontdict.txt", 'r+', encoding="utf-8") as f:
        f.seek(0, 0)
        for i in range(len(My_fonts)):
            f.write(str(My_fonts[i])+'\n')


deleteDict = {
    "FZLanTingHei-R-GBK": "方正黑体_GBK",
    "微软雅黑": "方正黑体_GBK",
    'cronos Pro Subhead': "方正黑体_GBK",
    'Arial': "方正黑体_GBK",
    '方正仿宋_GBK': "方正黑体_GBK",
    'hwKaiTi': "方正黑体_GBK",
    "迷你霹雳体": "迷你霹"
}


def relaceFont(txt1, changeFlag):
    deleteName = list(deleteDict.keys())
    relaceName = list(deleteDict.values())
    for i in range(len(deleteName)):
        if(deleteName[i] in txt1):
            txt = txt1.replace(deleteName[i], relaceName[i])
            txt1 = txt[:]
            print('replace %s with %s' %
                  (deleteName[i], relaceName[i]))
            changeFlag = 1
    return txt1, changeFlag


def removeUnnecessary(alltxt):
    """删除射手多余字幕"""
    txt = alltxt.split("\n")
    caqiangFlag = 0
    adFlag = 0
    for i in range(len(txt)-1, -1, -1):
        if("擦枪通用二" in txt[i]):
            del txt[i]
            caqiangFlag = 1
        elif("片头名单" in txt[i]):
            del txt[i]
            caqiangFlag = 1
        elif("看最新热播美剧" in txt[i]):
            del txt[i]
            caqiangFlag = 1
        elif("扫描即刻下载" in txt[i]):
            del txt[i]
            caqiangFlag = 1
        elif("pos(339.6,200)}■" in txt[i]):
            del txt[i]
            caqiangFlag = 1
        elif("pos(298.876,203.83)}■" in txt[i]):
            del txt[i]
            caqiangFlag = 1    
        elif(len(txt[i]) > 500):
            if(caqiangFlag == 1):
                del txt[i]
        elif("品牌广告推广合作  普罗米修斯" in txt[i]):
            del txt[i]
            adFlag = 1    

    if(caqiangFlag == 1):
        print("      擦枪字幕")
    if(adFlag == 1):
        print("      删除 普罗 广告")
    return txt


browserLabel = []


def readAssFile(Name, encodestyle, refreshFlag):
    with open("Fontdict.txt", 'r+', encoding="utf-8") as f:
        My_fonts = f.read()

    changeFlag = 0
    with open(Name, 'r+', encoding=encodestyle) as f:
        txt = f.read()
        # 替换字体
        txt, changeFlag = relaceFont(txt, changeFlag)
        # 删除射手字幕广告
        txtLines = removeUnnecessary(txt)

    # 重新写入文件
    if changeFlag == 1:
        with open(Name, 'w', encoding=encodestyle) as f:
            f.seek(0, 0)
            for i in range(len(txtLines)):
                f.write(txtLines[i])
                f.write("\n")
            print("rewrite")

    # 查找字体
    fontName = re.findall('fn(.*?)}', txt)
    styleFont = re.findall('Style: (.*?),(.*?),', txt)
    for i in range(len(styleFont)):
        fontName.append(styleFont[i][1])

    fontName = list(set(fontName))

    for i in range(len(fontName)):
        # print(fontName[i])
        if '\\' in fontName[i]:
            sub_s = fontName[i].find('\\')
            if sub_s == 0:
                # 为0是在中间的特效字体
                fontName[i] = fontName[i][3:]
                sub_s = fontName[i].find('\\')
                fontName[i] = fontName[i][:sub_s]
            else:
                fontName[i] = fontName[i][:sub_s]
    fontName = list(set(fontName))

    for i in range(len(fontName)):
        if fontName[i] in My_fonts:
            print('find', fontName[i])
        else:
            if refreshFlag == 'refreshed':
                if fontName[i] not in browserLabel:
                    # 无需重复打开同一个字体的搜索链接
                    browserLabel.append(fontName[i])
                    print('not find', fontName[i])
                    webAddress = "http://www.zitixiazai.org/plug/search.asp?key={}&x=17&y=12".format(
                        fontName[i])
                    webbrowser.open(webAddress)
            else:
                print('need refresh')
                return 'need refresh'
    print("\n")


def findFont(fileName):
    refreshFlag = 'not refreshed'
    # 使用不同的解码方式打开
    try:
        if(readAssFile(fileName, 'utf-8-sig', refreshFlag) == 'need refresh'):
            refreshFontList()
            print('refreshed')
            refreshFlag = 'refreshed'
            readAssFile(fileName, 'utf-8-sig', refreshFlag)

    except UnicodeDecodeError:
        if(readAssFile(fileName, 'utf-16', refreshFlag) == 'need refresh'):
            refreshFontList()
            print('refreshed')
            refreshFlag = 'refreshed'
            readAssFile(fileName, 'utf-16', refreshFlag)


if __name__ == '__main__':
    print(time.ctime())
    start = time.process_time()

    # 挑选字幕文件
    assFileName = os.listdir(os.getcwd())
    for i in range(len(assFileName)-1, -1, -1):
        if ".ass" not in assFileName[i]:
            assFileName.remove(assFileName[i])

    # 输出文件信息
    for i in range(len(assFileName)):
        print(assFileName[i])
        assInfo = (int)(
            (time.time() - os.stat(assFileName[i]).st_ctime)/60)
        if(assInfo < 60):
            print("     created %d mins ago" % assInfo)
        else:
            print("     created %d hours ago" % (assInfo/60))
        findFont(assFileName[i])

    # end 结束输出程序时间
    endTime = (time.process_time() - start)
    print("Time used:", endTime)
    time.sleep(0.5)
