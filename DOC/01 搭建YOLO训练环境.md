# 搭建YOLO环境

## 1 下载安装Anaconda

Anaconda 最大的作用其实就相当于python的虚拟环境，相当于docker，不同项目需要的包不一样，使用conda可以更好的进行项目管理

通过官网下载anaconda的exe安装包一路傻瓜式安装即可
这里注意两个点
1. 注意更换目录环境，默认一般都是选择c盘的，可以更换其他盘符
2. 注意将conda添加到path环境里面`Add Anaconda to my PATH environment variable`，虽然官方不推荐，但是真的会省很多事

## 2 下载Cudnn和CUDA

这里使用的是torch=1.2.0，官方推荐的Cuda版本是10.0，因此会用到cuda10.0，与cuda10.0对应的cudnn是7.4.1.5

这两个都可以在对应官网找到，但是因为某些原因，下载速度可能会非常慢，可以找国内的网盘分享

先打开cuda的安装包，按照引导一直下一步即可，注意选择自定义安装即可

安装完后在C盘这个位置可以找到根目录。

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0

然后大家把Cudnn的内容解压到cuda根目录下即可。

## 3 配置torch环境
Win+R启动cmd，在命令提示符内输入以下命令：
创建环境：
`conda create –n pytorch python=3.6`

激活环境：

`activate pytorch`

## 4 配置相关包

这一步可以直接在项目根目录激活环境后使用`pip install -r enquirement.txt`一键安装所需的包，但是这里有两个下载的可能比较慢，一个是`torch`，一个是`torchvision`，这两个可以单独安装。
相关轮子传网盘，下载完成进入相关路径**激活环境**后利用文件全名即可安装，具体命令如下

`pip install torch-1.2.0-cp36-cp36m-win_amd64.whl`

`pip install torchvision-0.4.0-cp36-cp36m-win_amd64.whl`



