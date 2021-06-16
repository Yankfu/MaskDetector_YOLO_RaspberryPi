# RPI.GPIO

## GPIO基本介绍
GPIO（General Purpose I/O Ports）意思为通用输入/输出端口，通俗地说，就是一些引脚，可以通过它们输出高低电平或者通过它们读入引脚的状态-是高电平或是低电平。GPIO是个比较重要的概念，用户可以通过GPIO口和硬件进行数据交互(如UART)，控制硬件工作(如LED、蜂鸣器等),读取硬件的工作状态信号（如中断信号）等。GPIO口的使用非常广泛。掌握了GPIO，差不多相当于掌握了操作硬件的能力。

## 控制GPIO
想用python来控制GPIO，最便捷的办法就是使用一些python类库，比如树莓派系统本身集成的RPi.GPIO。本文详细介绍如何使用RPi.GPIO来控制GPIO。

## 导入RPi.GPIO模块
可以用下面的代码导入RPi.GPIO模块。
`import RPi.GPIO as GPIO`
引入之后，就可以使用GPIO模块的函数了。


## 针脚编号
在RPi.GPIO中，同时支持树莓派上的两种GPIO引脚编号。第一种编号是BOARD编号，这和树莓派电路板上的物理引脚编号相对应。使用这种编号的好处是，你的硬件将是一直可以使用的，不用担心树莓派的版本问题。因此，在电路板升级后，你不需要重写连接器或代码。

第二种编号是BCM规则，是更底层的工作方式，它和Broadcom的片上系统中信道编号相对应。在使用一个引脚时，你需要查找信道号和物理引脚编号之间的对应规则。对于不同的树莓派版本，编写的脚本文件也可能是无法通用的。

可以使用下列代码（强制的）指定一种编号规则：

``` python
GPIO.setmode(GPIO.BOARD)
# or
GPIO.setmode(GPIO.BCM)
```

下面代码将返回被设置的编号规则
`mode = GPIO.getmode()`

如果RPi.GRIO检测到一个引脚已经被设置成了非默认值，那么你将看到一个警告信息。你可以通过下列代码禁用警告：
`GPIO.setwarnings(False)`

## 引脚设置
在使用一个引脚前，你需要设置这些引脚作为输入还是输出。配置一个引脚的代码如下：
``` python
# 将引脚设置为输入模式
GPIO.setup(channel, GPIO.IN)

# 将引脚设置为输出模式
GPIO.setup(channel, GPIO.OUT)

# 为输出的引脚设置默认值
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
```
## 释放
一般来说，程序到达最后都需要释放资源，这个好习惯可以避免偶然损坏树莓派。释放脚本中的使用的引脚：

`GPIO.cleanup()`
注意，GPIO.cleanup()只会释放掉脚本中使用的GPIO引脚，并会清除设置的引脚编号规则。

输出
要想点亮一个LED灯，或者驱动某个设备，都需要给电流和电压他们，这个步骤也很简单，设置引脚的输出状态就可以了，代码如下：

GPIO.output(channel, state)
状态可以设置为
 + 0 / GPIO.LOW / False 
 + 1 / GPIO.HIGH / True。
如果编码规则为，GPIO.BOARD，那么channel就是对应引脚的数字。

如果想一次性设置多个引脚，可使用下面的代码：
``` python
chan_list = [11,12]
GPIO.output(chan_list, GPIO.LOW)
GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   
```
你还可以使用Input()函数读取一个输出引脚的状态并将其作为输出值，例如：

`GPIO.output(12, not GPIO.input(12))`

我们也常常需要读取引脚的输入状态，获取引脚输入状态如下代码：

GPIO.input(channel)
低电平返回0 / GPIO.LOW / False，高电平返回1 / GPIO.HIGH / True。

## eg: 点亮二极管

``` python
import RPi.GPIO as GPIO  //引入函数库
import time

RPi.GPIO.setmode(GPIO.BOARD)  //设置引脚编号规则
RPi.GPIO.setup(11, RPi.GPIO.OUT)    //将11号引脚设置成输出模式

while True
    GPIO.output(channel, 1)   //将引脚的状态设置为高电平，此时LED亮了
    time.sleep(1)   //程序休眠1秒钟，让LED亮1秒
    GPIO.output(channel, 0)   //将引脚状态设置为低电平，此时LED灭了
    time.sleep(1)   //程序休眠1秒钟，让LED灭1秒

GPIO.cleanup()    //程序的最后别忘记清除所有资源
```
==========
到这里就是最后一步了
我们现在有可以获取视频的**mjpg-streamer**，有可以处理视频数据的**yolo**，有可以发送post请求的**request**
我们现在需要做的就是接收视频处理完后的post请求
这里使用flask搭建，因为没有过多的需求，只需要接收然后判断即可，判断完成后再点亮对应的二极管就完成任务了，具体实现在flaskLights.py里面，非常简单

同mjpg-streamer我们同样让这个后台运行就好
``` shell
nohup python flaskLights.py >> lights.log 2>&1 &
```