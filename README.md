# **追剧脚本 checkEpisodeUpdate**

    用来检测subhd.com上关注的美剧字幕是否更新来达到追剧的目的。若字幕组更新适配1080p的字幕，则发邮件提醒美剧更新，并打开字幕下载网页和在RARBG的搜索链接

## video_data中保存着美剧字幕的网站和第几集

    ### Example 绿箭侠
        [Arrow]
        url = http://subhd.com/zu0/14/d/26952101
        episode = 24

## myAccount中保存着Email的账户信息，也可以直接填在Email_Sender中

    ### example
        [Email]
        sendEmail = example@139.com  
        password = 123456789
        receiveEmail1 = example@126.com
        receiveEmail2 = example@outlook.com

# **检查特效字幕字体 findUninstalledFont**

    列举特效字幕.ass文件中的字体与系统中字体进行比对，若未找到则打开网页进行搜索
    播放器: MPC-HC