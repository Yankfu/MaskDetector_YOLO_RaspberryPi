# MaskDetector_YOLO_RaspberryPi

#### 介绍

基于YOLOv4的口罩识别系统，在树莓派上通过mjpg-streamer采集传输图像，使用YOLOv4进行目标检测。

使用前需要配置pytorch 1.2.0 和 cuda 10.0

#### 软件架构

主要由两个开源项目构成：

+ 一个是Bubbliiiing大佬的yolov4-pytorch，对新手非常友好，可以从零开始学习如何训练自己的模型，B站也有账号和教程

  git地址：https://github.com/bubbliiiing/yolov4-pytorch

  B站地址：https://www.bilibili.com/video/BV1Q54y1D7vj

+ 另一个是mjpg-streamer，用于远程视频展示

  git地址：https://github.com/jacksonliam/mjpg-streamer

