#-------------------------------------#
#   调用摄像头或者视频进行检测
#   调用摄像头直接运行即可
#   调用视频可以将cv2.VideoCapture()指定路径
#   视频的保存并不难，可以百度一下看看
#-------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image
import changeRaspColor

from yoloReturn2 import YOLO
# from changeRaspColor import ChangeColor

# 这里给yolo的return添加了一个参数label，如果检测到大于一个未佩戴口罩的就调用函数
def changeColor(labels):
    len = 0
    for i in labels:
        findMask = str(i, encoding = "utf-8")
        if findMask.find("no_mask") != -1:
            len += 1

    if len > 0 :
        changeRaspColor.changeLightsColor("01")
    if len == 0 :
        changeRaspColor.changeLightsColor("10")

yolo = YOLO()
#-------------------------------------#
#   调用摄像头
#   capture=cv2.VideoCapture("1.mp4")
# http://192.168.1.147:8080/?action=stream
#-------------------------------------#
capture=cv2.VideoCapture(0)
# capture=cv2.VideoCapture("http://192.168.1.147:8080/?action=stream")
fps = 0.0
while(True):
    t1 = time.time()
    # 读取某一帧
    ref,frame=capture.read()
    # 格式转变，BGRtoRGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))
    # 进行检测
    img,labels = yolo.detect_image(frame)
    changeColor(labels)
    frame = np.array(img)
    # RGBtoBGR满足opencv显示格式
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

    fps  = ( fps + (1./(time.time()-t1)) ) / 2
    print("fps= %.2f"%(fps))
    frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("video",frame)

    c= cv2.waitKey(1) & 0xff 
    if c==27:
        capture.release()
        break
