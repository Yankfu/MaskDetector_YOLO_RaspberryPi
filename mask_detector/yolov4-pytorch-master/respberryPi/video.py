import flask, json
import uuid
from flask import request
from PIL import Image
import base64
server = flask.Flask(__name__)
@server.route('/', methods=['get', 'post'])
def sendPicture():
    # 从摄像头读取照片
    # 返回照片
    

@server.route('/getRes', methods=['get', 'post'])
def showLight():
    # 接收返回参数
    # 点灯
    print("-----")

if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')