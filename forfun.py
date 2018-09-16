import io
import sys
import os



def readAssFile(Name, encodestyle):
    with open(Name, 'r+', encoding=encodestyle) as f:
        txt = f.read()
        if 'FZLanTingHei-R-GBK' in txt:
            print('FZLanTingHei')
            txt1=txt.replace("FZLanTingHei-R-GBK","方正黑体_GBK")
            print('replace FZLanTingHei with 方正黑体_GBK')
            f.seek(0, 0)  
            f.write(txt1)

def findFont(fileName):
        try:
            readAssFile(fileName, 'utf-8-sig')

        except UnicodeDecodeError:
            readAssFile(fileName, 'utf-16')

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

for i in range(len(assFileName)):
    print(assFileName[i])
    findFont(assFileName[i])

with open("Fontdict.txt", 'r+') as f:
    txt = f.read()
    fontlist = txt.split(',')
    print(fontlist)
