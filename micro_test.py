import time
import difflib
import re


def compareStr(str1, str2):
    return (difflib.SequenceMatcher(None, str1, str2).quick_ratio())


startTime = time.process_time()

assName = "Legends.of.Tomorrow.S04E06.Tender.is.the.Nate.1080p.Amazon.WEB-DL.DD+5.1.H.264-QOQ.ass"
with open(assName, 'r+', encoding='utf-8-sig') as f:
    txt = f.read().split("\n")

# for i in range(len(txt)-1):
for i in range(200):
    if(len(txt[i]) > 7):
        if txt[i][0] == 'D':
            Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text = txt[i][12:].split(
                ',', 8)
            if r"\N" in Text:
                chineseText, englishText = Text.split(r"\N", 1)
            elif r"\n" in Text:
                chineseText, englishText = Text.split("\n", 1)
            else:
                chineseText = "$这里是特效$"
                englishText = Text
                # print("\n split chinses and english error")
                # print(txt[i])
                

            # print(compareStr(Text,Text[60:]))
            if chineseText != "$这里是特效$":
                if '}' in englishText:
                    sub_s = re.search('.*}', englishText).span()
                    englishText = englishText[sub_s[1]:]
                # englishText=englishText[sub_s:]
            print("%s  %s  $lineNumber=%d" % (chineseText, englishText, i))


# print(txt[1])
# h, m, s = assSting.split(':', 2)
# print(h)
# print(m)
# print(s)
# s, cs = s.split('.',1)

# print(s)


endTime = (time.process_time() - startTime)
print("Time used: %f" % (endTime))
