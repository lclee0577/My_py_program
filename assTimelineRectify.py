import time
import re

start = time.process_time()
TimeList=[]
content=[]
srtName = 'Supergirl.S04E07.Rather.the.Fallen.Angel.1080p.Amazon.WEB-DL.DD+5.1.H.264-QOQ.srt'
assName = "Supergirl.S04E07.720p.HDTV.x264-AVS.简体&英文.ass"
with open(srtName, 'r+',encoding='utf-8') as f:
    txt = f.read().split("\n\n")
    
for i in range(len(txt)-1):
        txtSplit = txt[i].split("\n") 
        endTime = txtSplit[1][-12:]
        temp = int(endTime[-3:])/100*6
        endTime = "%s.%02d"%(endTime[1:-4],temp)
        
        startTime = txtSplit[1][:12]
        temp = int(startTime[-3:])/100*6
        startTime = "%s.%02d"%(startTime[1:-4],temp)

        TimeList.append('%s,%s'%(startTime,endTime))
        
        if '{\\an8}' in txtSplit[2]:
            txtSplit[2] = txtSplit[2].replace("{\\an8}","")
        content.append(txtSplit[2])

findtimelist = []
reserveCount = 0
with open(assName, 'r+', encoding='utf-8-sig') as f:
    txt = f.read().split("\n")
    
    
    for j in range(len(txt)):   
        slitTemp = txt[j].split(",,")
        if len(slitTemp) == 2:
            if slitTemp[1][0] != "{":
                sub_s = slitTemp[1].find('\\')
                temp =slitTemp[1][:sub_s]
                
            for i in range(reserveCount,len(content)):
                if(content[i] == temp):
                    # print(txt[j])
                    findTime = txt[j][11:33]
                    if findTime[0]==",":
                        findTime = findTime[1:]
                    if findTime[-1]==",":
                        findTime = findTime[:-1]
                    findtimelist.append(findTime)
                    txt[j]=txt[j].replace(findTime,TimeList[i])
                    reserveCount = i 
                    break
                # print(TimeList[1])
                # print(txt[j])

with open('123.ass', 'a', encoding='utf-8-sig') as f:
    f.seek(0,0)
    for i in range(len(txt)):
    # for i in range(30):
        f.write(txt[i])
        f.write("\n")

endTime = (time.process_time() - start)
print("Time used:", endTime)

