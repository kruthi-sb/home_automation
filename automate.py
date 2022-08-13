import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)

living_room = 38 #stonewolf
study_room = 36 #werewolf 
kitchen = 32 #pumpkin
all_lights = [38, 36, 32] #monstermash
GPIO.setmode(GPIO.BOARD)
relay = all_lights
for x in relay:
    GPIO.setup(x, GPIO.OUT)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'all_lights':
        if deviceName == 'living_room':
            num  = 38
        if deviceName == 'study_room':
            num  = 36
        if deviceName == 'kitchen':
            num  = 32
 
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(num, GPIO.OUT)
        GPIO.output(num, GPIO.LOW)
        #time.sleep(5)
        #GPIO.output(num, GPIO.HIGH)
    else:
        relay = all_lights
        for x in relay:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(x, GPIO.OUT)
            GPIO.output(x, GPIO.LOW)
        time.sleep(5)
        for x in relay:
            GPIO.output(x, GPIO.HIGH)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
