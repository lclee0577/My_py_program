import io
import sys
import os

import wx
from wx import  FontEnumerator 
 

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

aaa =wx.App(False)
e = wx.FontEnumerator()
fontList = e.GetFacenames()
for i in fontList:
    print(i)