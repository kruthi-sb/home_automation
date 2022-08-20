✨Home Automation using Raspberrypi - 3B✨

📜Description: 
This is a small automation project created using raspberrypi and relay board.
We used 3 bulbs signifying 3 rooms in a home to demonstrate this project.
The Main file basically creates a webpage through which you and I can control our devices from the comfort of our phones.
In the movement detection file, the code uses a webcam to detect any movements in a room  and turn on or off the room lights accordingly. This was just a test.
We referred vidoes from NetworkChuck in making this project.

✨How to use this project:

👉You'll need:
1. Raspberrypi Model 3B with raspbian OS installed
2. Relay board with atleast 3 inputs
3. Jumper wires
4. Bulb sockects and bulbs
5. Electrical wires with a plug

👉You can refer the following videos by NetworkChuck:
1. To setup raspberrypi: https://www.youtube.com/watch?v=vbaJcRxASo0
   🔴NOTE: you need to have static IP for Pi. Watch the above video for doing so.
2. Automation: https://www.youtube.com/watch?v=B_krqlk_cXo

👉Connections:
Refer the diagram attached for the connections between Pi and relay board
The connection of the bulbs must be in parallel connection. Refer the video 2 for greater insights.

👉The code:
1. While in the Terminal of Pi, you'll need to create a new folder(say, automation).
2. Inside automation, create folders named exactly as 'templates' and 'static'
3. Create new file named index.html inside templates and copy paste the code from index.html file here.
4. Create new file named style.css inside static and copy paste the code from style.css file here.
5. Now, create a new file inside automation with name main.py and copy paste the code from main.py file here.
6. You're ready to go! run the file main.py
7. Type your static IP address in your fav browser and search. You should get the home controller page!

✨CREDITS:
Kruthi S B: https://github.com/kruthi-sb 
Nitisha Patil: https://github.com/Nitisha-Patil
