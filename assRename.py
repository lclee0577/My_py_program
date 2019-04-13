import os
import time
import re
import shutil

def reName():
    allname = os.listdir(os.getcwd())
    for each in allname:
        assName = re.match(r'(.*?)\.(S\d+E\d+)(.*?).ass', each)
        if(assName):
            epso=assName.group(2)
            mod = r"(.*?)\.{}(.*?).mkv".format(epso)
            for each in allname:
                mkvfile = re.match(mod,each)
                if(mkvfile):
                    writeName = mkvfile.group().replace(".mkv",".ass")
                    if(os.path.exists(assName.group())):
                         shutil.move(assName.group(),writeName)

if __name__ == '__main__':
    print(time.ctime())
    start = time.process_time()
    reName()
    timeUse=time.process_time() -start
    print("time use ",timeUse)
