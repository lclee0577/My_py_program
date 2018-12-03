import cv2

if __name__ == '__main__':
    rgb_img = cv2.imread("123.jpg")
    cv2.imshow('rgb_img', rgb_img)
    """ 读取图片并显示"""

    yuv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2YUV)
    yImg, uImg, vImg = cv2.split(yuv_img)
    """ 颜色空间转换并提取Y，U，V分量 """

    for i in range(len(yImg)):
        yImg[i] = 255 - yImg[i]
    """ 反色 """

    for i in range(len(uImg)):
         vImg[i] = uImg[i] = 128
    """  去色  """

    yuv_img = cv2.merge([yImg, uImg, vImg])
    yuv_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2RGB)
    cv2.imshow('yuv_img', yuv_img)
    """  合并Y,U,V分量 转换到RGB空间来显示 """

    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
        