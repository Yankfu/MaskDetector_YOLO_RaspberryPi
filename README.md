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

### YOLOv4部分

#### 训练出第一个你自己的模型

首先是YOLOv4部分，数据集需要自己收集或者使用网上开源数据集，本次口罩识别所用到的数据集放到百度网盘，可自取，地址：==百度网盘地址==。

1. 本文使用VOC格式进行训练。 

2. 训练前将标签文件放在VOCdevkit文件夹下的VOC2007文件夹下的Annotation中。 

3. 训练前将图片文件放在VOCdevkit文件夹下的VOC2007文件夹下的JPEGImages中。 

4. 在训练前利用voc2yolo4.py文件生成对应的txt。 

5. 再运行根目录下的voc_annotation.py，运行前需要将classes改成你自己的classes。**注意不要使用中文标签，文件夹中不要有空格！**  

6. 此时会生成对应的2007_train.txt，每一行对应其**图片位置**及其**真实框的位置**。 

7. **在训练前需要务必在model_data下新建一个txt文档，文档中输入需要分的类，在train.py中将classes_path指向该文件。**
8. 运行train.py即可开始训练。

#### 预测步骤

##### a、使用预训练权重

1. 下载完库后解压，在百度网盘下载yolo4_weights.pth或者yolo4_voc_weights.pth，放入model_data，运行predict.py，输入 

   ```python
   img/street.jpg
   ```

   

2. 利用video.py可进行视频检测，默认0开启摄像头，也可以输入视频路径。 

##### b、使用自己训练的权重

1. 按照训练步骤训练。 

2. yolo.py文件里面，在如下部分修改model_path和classes_path使其对应训练好的文件；**model_path对应logs文件夹下面的权值文件，classes_path是model_path对应分的类**。 

   ```python
   _defaults = {
       "model_path": 'model_data/yolo4_weights.pth',
       "anchors_path": 'model_data/yolo_anchors.txt',
       "classes_path": 'model_data/coco_classes.txt',
       "model_image_size" : (416, 416, 3),
       "confidence": 0.5,
       "cuda": True
   }
   ```

   

3. 运行predict.py，输入 

   ```python
   img/street.jpg
   ```

4. 利用video.py可进行视频检测，默认0开启摄像头，也可以输入视频路径。 

### 树莓派部分

[树莓派选购](..\DOC\树莓派选购.md)

