import RPi.GPIO as GPIO

living_room = 38 
study_room = 36 
kitchen = 32 
all_lights = [38, 36, 32] 
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
       
        if deviceName == 'living_room_off':
            num = 38
            GPIO.output(num, GPIO.HIGH)
        if deviceName == 'study_room_off':
            num = 36
            GPIO.output(num, GPIO.HIGH)
        if deviceName == 'kitchen_off':
            num = 32
            GPIO.output(num, GPIO.HIGH)


    else:
        relay = all_lights
        if deviceName == 'all_lights':
            for x in relay:
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(x, GPIO.OUT)
                GPIO.output(x, GPIO.LOW)
        
        if deviceName == 'all_lights_off':
            for x in relay:
                GPIO.output(x, GPIO.HIGH)

    return render_template('index.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
