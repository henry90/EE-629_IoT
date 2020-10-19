# EE-629_IoT
Weekly Reports<br/>
[2020-10-13] • Continue with the LED Matrix project.<br>
There are 8x8 LED Matrix generator tools online, but it displays in reversed and 90 degrees clockwise rotate orientation on the LED Matrix due to they are other types of LED Matrix. For example, I draw a letter "N", and the code is 0x86,0xc6,0xc6,0xe6,0xf6,0xde,0xce,0xc6, # "N" . This is how it shows on the LED.<br>
<br>
![](notN.jpg)<br>
<br>
The LED Matrix I am using is a Common Anode LED Matrix. There are 8 columns. Each column is represented by one byte. In Binary, 0 is LEDs turned OFF, and 1 is LEDs turned ON. Too draw a diagram, convert each column from Binary number to Hexadecimal code at here: https://www.rapidtables.com/convert/number/binary-to-hex.html , and add "0x" before the converted Hexadecimal code.<br>
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
[2020-09-08] Installed lastest release of Raspbian operating system on Raspberry Pi 3B. Assembled Raspberry Pi 3B with the Google AIY: Voice Kit https://aiyprojects.withgoogle.com/voice/.<br/>
