import cv2
n = []
p = []
s = []
r = []

if __name__ == '__main__':
    rgb_img = cv2.imread("12345.jpg")
    cv2.imshow('rgb_img', rgb_img)

    yuv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2YUV)
    yImg, uImg, vImg = cv2.split(yuv_img)
    for i in range(len(uImg)):
            vImg[i] = uImg[i] = 128
    """  去色 """

    yuv_img = cv2.merge([yImg, uImg, vImg])
    yuv_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2RGB)
    cv2.imshow('gray_img', yuv_img)
    """ 显示均衡化前的黑白图像 """

    for i in range(256):
        n.append(0)
        p.append(0)
        s.append(0)
        r.append(0)

    for i in range(len(yImg)):
        for j in range(len(yImg[i])):
            k = yImg[i][j]
            k = int(k)
            n[k] += 1
    
    for k in range(256):
        p[k] = n[k]/(len(yImg)*len(yImg[0]))

    s[0]=p[0]
    for k in range(1,256):
        s[k]=s[k-1]+p[k]

    for k in range(256):
        r[k] = int(s[k]*255)

    for i in range(len(yImg)):
        for j in range(len(yImg[i])):
            k = yImg[i][j]
            k = int(k)
            yImg[i][j] = r[k]


    yuv_img = cv2.merge([yImg, uImg, vImg])
    yuv_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2RGB)
    cv2.imshow('yuv_img', yuv_img)
    """  合并Y,U,V分量 转换到RGB空间来显示 """

    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
        