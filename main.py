import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
import numpy as np
import datetime


'''def detect():
    cam = cv2.VideoCapture(0) # Videocapture is a function of opencv which allows capturing image
    
    
    ret, frame1 = cam.read() # reading image 'frame by frame' 
    ret, frame2 = cam.read() # reading change in image and deciding region of interest or 'roi'
    diff = cv2.absdiff(frame1, frame2) # detecting difference in both frames
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) # setting  grayscale parameters for image captured 
    cv2.imshow('Camera', gray) # showing the change captured by camera
    cv2.waitKey(10000) # waiting till the next function is called
    print(np.all(gray==0))    

    return gray'''


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
    if deviceName != 'all_lights' and deviceName != 'all_lights_off':
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
        if deviceName == 'living_room_off':
            num = 38
            GPIO.output(num, GPIO.HIGH)
        if deviceName == 'study_room_off':
            num = 36
            GPIO.output(num, GPIO.HIGH)
        if deviceName == 'kitchen_off':
            num = 32
            GPIO.output(num, GPIO.HIGH)
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(num, GPIO.OUT)
        


    else:
        relay = all_lights
        if deviceName == 'all_lights':
            for x in relay:
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(x, GPIO.OUT)
                GPIO.output(x, GPIO.LOW)
        #time.sleep(5)
        if deviceName == 'all_lights_off':
            for x in relay:
                GPIO.output(x, GPIO.HIGH)

    return render_template('index.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    '''detect()
    hour = int(datetime.datetime.now().hour)
    if np.all(gray==0) is False: #and hour>18
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(36, GPIO.OUT)
        GPIO.output(36, GPIO.LOW)
        time.sleep(10)
        GPIO.output(36, GPIO.HIGH)'''






