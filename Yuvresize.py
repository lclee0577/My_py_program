import cv2
import math
import numpy as np
import time
resizeCeo = 1.3
if __name__ == '__main__':
    print(time.ctime())
    start = time.process_time()
    rgb_img = cv2.imread("12345.jpg")
    cv2.imshow('rgb_img', rgb_img)
    yuv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2YUV)
    yImg, uImg, vImg = cv2.split(yuv_img)
    rowLen,colLen = yImg.shape
    resizeH = int(np.floor(resizeCeo*rowLen))
    resizeW = int(np.floor(resizeCeo*colLen))
    """计算变换后大小"""
    newYImg = np.array([[0]*resizeW for i in range(resizeH)],dtype=np.uint8)
    newYImg2 = np.ones(newYImg.shape[:2],dtype="uint8")
    newUImg = np.ones(newYImg.shape[:2],dtype="uint8")
    newVImg = np.ones(newYImg.shape[:2],dtype="uint8")
    """初始化数组"""
    for i in range(resizeH):
            for j in range(resizeW):
                floatX = i/resizeCeo
                floatY = j/resizeCeo
                floorX = int(math.floor(floatX))
                floorY = int(math.floor(floatY))
                newVImg[i][j] = 128
                newUImg[i][j] = 128
                """U，V分量取128，转化为灰度图像"""
                newYImg2[i][j] =yImg[floorX][floorY]
                """临近差值"""

                if (floorX == rowLen-1) or(floorY == colLen-1):
                    newYImg[i][j] =yImg[floorX][floorY]
                    """边界处无需再计算，直接取边界值即可"""
                else:
                    interpCeoW = floatX - math.floor(floatX)
                    interpCeoH = floatY - math.floor(floatY)
                    newYImg[i][j] = (1-interpCeoH)*(1-interpCeoW)*yImg[floorX]  [floorY]
                    newYImg[i][j] +=(1-interpCeoH)*(interpCeoW)  *yImg[floorX+1]  [floorY]
                    newYImg[i][j] +=(interpCeoH)*(1-interpCeoW)  *yImg[floorX][floorY+1]
                    newYImg[i][j] +=(interpCeoH)*(interpCeoW)    *yImg[floorX+1][floorY+1]
                    """双线性差值"""

    yuv_img = cv2.merge([newYImg, newUImg, newVImg])
    yuv_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2RGB)
    cv2.imshow('yuv_img', yuv_img)
    yuv_img2 = cv2.merge([newYImg2, newUImg, newVImg])
    yuv_img2 = cv2.cvtColor(yuv_img2, cv2.COLOR_YUV2RGB)
    cv2.imshow('yuv_img2', yuv_img2)
    """  合并Y,U,V分量 转换到RGB空间来显示 """
    endTime = (time.process_time() - start)
    print("Time used:", endTime)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()