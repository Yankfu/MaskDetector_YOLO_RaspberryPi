# 网络摄像头

## 1 将项目传到树莓派上
xftp可以直接传zip文件，在同名文件下
ssh连接上了也可以直接clone项目到本地

## 2 编译

这里插一段原文

Building & Installation
=======================

You must have cmake installed. You will also probably want to have a development
version of libjpeg installed. I used libjpeg8-dev. e.g.

    sudo apt-get install cmake libjpeg8-dev

If you do not have gcc (and g++ for the opencv plugin) you may need to install those.

    sudo apt-get install gcc g++

Simple compilation
------------------

This will build and install all plugins that can be compiled.

    cd mjpg-streamer-experimental
    make
    sudo make install

在保证本机有cmake和gcc后

进入项目目录

再编译项目即可

## 启动项目

``` shell
 ./mjpg_streamer -i "./input_raspicam.so" -o "./output_http.so -w ./www"
```

不过一般是后台启动的，可以输入这个

``` shell
nohup ./mjpg_streamer -i "./input_raspicam.so" -o "./output_http.so -w ./www" >> output.log 2>&1 &
```

想结束可以通过`ps ef`查看pid直接kill