
import webbrowser
import time
import pyautogui
"""
用于自动转移淘宝购买的百度文库积分
"""
websitelist=['https://wenku.baidu.com/view/d5be963f5727a5e9856a61f6',
                'https://wenku.baidu.com/view/6517da94dd88d0d233d46af8',
                'https://wenku.baidu.com/view/f0533511f18583d049645960',
                'https://wenku.baidu.com/view/06586a64783e0912a2162a74',
                'https://wenku.baidu.com/view/c9131daedd3383c4bb4cd277',
                'https://wenku.baidu.com/view/20423e83f7ec4afe05a1df53',
                'https://wenku.baidu.com/view/6dd05e372cc58bd63086bda9',
                'https://wenku.baidu.com/view/80171c943086bceb19e8b8f67c1cfad6185fe944',
                'https://wenku.baidu.com/view/cff0b822dcccda38376baf1ffc4ffe473268fd47',
                'https://wenku.baidu.com/view/c71c3685ab00b52acfc789eb172ded630a1c9847',
                'https://wenku.baidu.com/view/f9fc9724f4335a8102d276a20029bd64793e6244',
                'https://wenku.baidu.com/view/70242d4f4b7302768e9951e79b89680202d86b44',
                'https://wenku.baidu.com/view/580213674a35eefdc8d376eeaeaad1f347931144',
                'https://wenku.baidu.com/view/cff0b822dcccda38376baf1ffc4ffe473268fd47',
                'https://wenku.baidu.com/view/0924eb5efbd6195f312b3169a45177232e60e444',
                 'https://wenku.baidu.com/view/0924eb5efbd6195f312b3169a45177232e60e444',
                 ]
'''网址填这里'''            

pyautogui.FAILSAFE = True
loopCount = 0

def autoClick(subsite):

    webbrowser.open("http://www.blpack.com")
    time.sleep(1.5)
    pyautogui.click(765, 796)
    '''这里填网页里文档链网址输入框的坐标'''

    pyautogui.typewrite(str(subsite))
    time.sleep(1)
    pyautogui.click(189, 1093)
    '''提交按钮坐标'''

    time.sleep(1)
    pyautogui.click(1375, 573)
    '''下载按钮坐标'''

    time.sleep(3)
    pyautogui.hotkey('ctrlleft','w')

if __name__ == '__main__':

    for i in range(len(websitelist)):
        autoClick(websitelist[i])
    # while 1:
    #     print(pyautogui.position())
    #     time.sleep(0.25)
