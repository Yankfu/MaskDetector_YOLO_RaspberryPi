from flask import Flask, request, jsonify
import json
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
chan_list = [23, 24]
GPIO.setup(chan_list, GPIO.OUT)

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['post'])
def add_stu():
    mask = request.form.get('mask')
    if mask == "01":
        GPIO.output(chan_list, (True, False))
        return "Color change to blue"
    if mask == "10":
        GPIO.output(chan_list, (False, True))
        return "Color change to red"
    if mask == "00":
        GPIO.output(chan_list, (False, False))
        return "Turn off all lights"
    if mask == "11":
        GPIO.output(chan_list, (True, True))
        return "Turn on all lights"
    return "error"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
