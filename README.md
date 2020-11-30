# EE-629_IoT
Weekly Reports<br/>
[2020-11-23] Change of Project: I2C LCD Display.<br>
Display CPU temputure, and time.<br>
![](I2C_LCD-tempTime.png)<br>
Next: Weather.<br>
:<br>
[2020-11-16] Compeleted Blockchain demos.<br>
• Final Project: 4WD Raspberry Pi Robot.<br>
Assembled the robot. Retuned the tracking module sensors and light seeking module sensors.<br>
![](4wd-pi-robot.png)<br>
:<br>
[2020-11-09] Installed pyang, PlantUML, GIMP, Pinta and ran the demos on Raspberry Pi.<br>
Updated to macOS Big Sur. Experiencing issues due to unsupported version. Working on it...<br>
:<br>
[2020-11-02] Installed Python packages which introduced at lession 8 on Mac and Raspberry Pi.<br>
Installed XQuartz on Mac for SSH -Y.<br>
Ran Data Analysis Python demo codes.<br>
• Thermometer<br>
Components: Thermistor, ADC module, Jumper wires, and Resistors 10kΩ.<br>
 Enable I2C and Installed I2C tools:<br>
sudo raspi-config<br>
 Choose “5 Interfacing Options” then “P5 I2C” then “Yes” and then “Finish” in this order and restart Raspberry Pi<br>
 Check whether the I2C module is started:<br>
lsmod | grep i2c<br>
 Install I2C-Tools:<br>
sudo apt-get install i2c-tools<br>
 I2C device address detection:<br>
i2cdetect -y 1<br>
 Ran the Python program, but it shows errors.<br>
![](thermo_errors.png)<br>
:<br>
[2020-10-26] Logged in ThingSpeak using MathWorks account. Created cpu_loop channel.<br>
Created rpidata project with Google Drive and Sheets API and credentials on Google Cloud Platform.<br>
Installed gspread, oauth2client, and psutil on Raspberry Pi.<br>
Ran and tested lab programs.<br>
:
[2020-10-19] 
• Signed up an Particle account<br>
• Installed Particle-Agent on Raspberry Pi and logged into the Particle account<br>
• Added Raspberry Pi device in the Particle account<br>
• Original link of the Particle Mobile App in the lecture slides does not work. Found supporting document: https://docs.particle.io/tutorials/developer-tools/tinker/photon/<br>
<br>
• Installed Particle iOS app and connected to Raspberry Pi<br>
• Installed node.js and npm on Raspberry Pi<br>
Step1: Update Pi<br>
sudo apt-get update<br>
Step 2: Identify Architecture Version of Raspberry Pi 3 /3B+: ARMv7<br>
Step 3: Copy the ARMv7 download link at NodeJS downloads page<br>
Step 4: Go to terminal to download NodeJS Binaries<br>v
Wget https://nodejs.org/dist/v12.19.0/node-v12.19.0-linux-armv7l.tar.xz <br>
Step 5: Extract the downloaded file<br>
tar -xf node-v12.19.0-linux-armv7l.tar.xz<br>
Step 6: Copy the files to a directory in PATH<br>
cd node-v12.19.0-linux-armv7l<br>
sudo cp -R * /usr/local/<br>
Step: 6: Check if installation was successful<br>
pi@raspberrypi:~ $ node -v<br>
v12.19.0<br>
pi@raspberrypi:~ $ npm -v<br>
6.14.8<br>
<br>
• Installed PARTICLE CLI<br>
• Installed Node-RED and run on http://localhost:1880<br>
• Run node lesson 6 hello.js<br>
Server running at http://127.0.0.1:8080/<br>
Inspected the webpage. Less than 200ms loading time. Favicon.ico loads after.<br>
• Run node http.js<br>
No response<br>
• Installed node.js, npm, Particle-CLI, and Atom on laptop<br>
• Installed MATLAB on Android phone. Toggled on all of the sensors and moving around the phone, observes the data changes.<br>
:<br>
[2020-10-13] • Continue with the LED Matrix project.<br>
There are 8x8 LED Matrix generator tools online, but it displays in reversed and 90 degrees clockwise rotate orientation on the LED Matrix due to they are other types of LED Matrix. For example, I drew the letter "N", and the code is 0x86,0xc6,0xc6,0xe6,0xf6,0xde,0xce,0xc6, # "N" . This is how it shows on the LED.<br>
<br>
![](notN.jpg)<br>
<br>
The LED Matrix I am using is a Common Anode LED Matrix. There are 8 columns. Each column is represented by one byte. In Binary, 0 is LEDs turned OFF, and 1 is LEDs turned ON. To draw a diagram, convert each column from Binary number to Hexadecimal code at here: https://www.rapidtables.com/convert/number/binary-to-hex.html , and add "0x" before the converted Hexadecimal code.<br>
Diagram below from Freenove.<br>
![](LED_Matrix_Binary_Hex.png)<br>
This is the correct code for letter "N": 0x00,0xFF,0x60,0x30,0x18,0x0C,0x06,0xFF, # "N" .<br>
![](N.jpg)<br>
:<br/>
[2020-10-07] LED Projects (Codes and instructions from Freenove):<br>
① Blinking Red LED.<br>
Hardware and electronic components:<br>
• Raspberry Pi 3B<br>
• Breadboard<br>
• GPIO Extension Board<br>
• 220Ω Resister<br>
• Red LED<br>
• Jump Wires (M-M)<br>
<br>
![](Blinking_Red_LED.gif)<br>
<br>
② Display numbers and letters on LED Matrix display.<br>
Hardware and electronic components:<br>
• Raspberry Pi 3B<br>
• Breadboard<br>
• GPIO Extension Board<br>
• 8x8 LED Matrix<br>
• 220Ω Resisters<br>
• 74HC595 DIP IC<br>
• Jump Wires (M-M)<br>
<br>
![](LED_Matrix.gif)<br>
:<br/>
[2020-09-29] Purchased starter kit for Raspberry Pi including breadboard and all sort of electronic components. Reconfigured the Google Cloud due to billing issues.<br/>
:<br/>
[2020-09-22] Installed VNC Viewer on Raspberry Pi and Mac. Successfully connected to Raspberry Pi using VNC Viewer and Secure Shell. Push the Red button to talk to Google Assistant, with audio and text feedback.<br/>
:<br/>
[2020-09-15] Reviwed the lecture and followed the instruction to configure the system settings. Modified the Digital Clock Setting: %a  %h %d  %I:%M %p. For example it will display: Tue Sep 15 10:00 AM. Connect Mac to the Raspberry Pi using Google Chrome extension: Secure Shell https://chrome.google.com/webstore/detail/secure-shell/iodihamcpbpeioajjeobimgagajmlibd. Get the crdiential from Google Cloud Speech APIs. https://console.cloud.google.com/.<br/>
:<br/>
[2020-09-08] Used Etcher https://www.balena.io/etcher/ to flash the Raspbian operating system onto the MicroSD card. Assembled Raspberry Pi 3B with the Google AIY: Voice Kit https://aiyprojects.withgoogle.com/voice/.<br/>
