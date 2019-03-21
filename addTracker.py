import torrent_parser as tp
import wget
import os
import time
import copy



def updataTrackList():
    modifyTime = (time.time() - os.stat("trackers_best.txt").st_mtime)
    if(modifyTime>(24*60*60)):
        if(os.path.exists("trackers_best.txt")):
                os.unlink("trackers_best.txt")
        filename = wget.download("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt") 
        print("refresh tracker list")   

    with open("trackers_best.txt","r") as f:
        bestTrackList = f.read().split("\n\n")
        bestTrackList.remove("")

    return bestTrackList

def addTracker(btFileName,trackList):
    data = tp.parse_torrent_file(btFileName)
    track = data['announce-list']
    for each in track:
        if each[0] in trackList:
            trackList.remove(each[0])

    if(len(trackList)>0):
        print("add new track ",len(trackList))
        for i in range(len(trackList)):
            track.append(trackList[i:i+1])
            
        tp.create_torrent_file(btFileName, data)

    else:
        print("there is nothing to add",btFileName)

    
bestTrackList = updataTrackList()
btFileName = os.listdir(os.getcwd())
for i in range(len(btFileName)-1, -1, -1):
    if ".torrent" not in btFileName[i]:
        btFileName.remove(btFileName[i])
        
for eachBT in btFileName:
    addTracker(eachBT,copy.copy(bestTrackList))