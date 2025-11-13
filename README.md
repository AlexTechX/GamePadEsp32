🎮 GamePad ESP32 – User Guide
1. Project Description

This project is a wireless controller based on the ESP32 to play Blasphemous or other keyboard-controlled games.
It uses 14 physical buttons and communicates via Wi-Fi with a Python application that converts the button signals into configurable keyboard inputs.

2. Requirements

Hardware:

ESP32 (38 pins)

14 push buttons

Wires and breadboard (optional)

Software:

Arduino IDE (to upload the .ino file)

Python 3.12+

Python libraries: pynput, websocket-client

Local Wi-Fi connection

3. Download the Project

Open Git Bash, CMD, or PowerShell.

Clone the repository:

git clone https://github.com/AlexTechX/GamePadEsp32.git


Navigate into the project folder:

cd GamePadEsp32

4. Configure and Run the Python Application

Install the required Python libraries:

pip install pynput websocket-client


Connect to the ESP32 Wi-Fi network.

Run the Python script:

python mando_blasphemous.py


The graphical interface will open where you can:

Assign keys to each button

Save the configuration to config.json

Note: Special keys like space, enter, shift, etc., are automatically interpreted.

5. Upload the Arduino Sketch to the ESP32

Open Arduino IDE.

Load the file Gamepad.ino.

Select:

Board → ESP32

COM port → your ESP32 port

Click Upload.

Open the Serial Monitor to check the ESP32 IP address (e.g., 192.168.4.1).

6. Wiring Guide

Connect each button between the assigned ESP32 GPIO pin and GND.

Function	GPIO	Default Key
UP	32	w
DOWN	33	s
LEFT	12	a
RIGHT	26	d
ATTACK	25	k
DASH	27	l
PRAYER	13	j
USE_VESSEL	14	f
JUMP	4	space
START	16	enter
SELECT	17	shift
ITEM1	5	q
ITEM2	18	e
ITEM3	19	r

Notes:

One terminal of the button → assigned GPIO

Other terminal → GND

No external resistor is needed; the code uses INPUT_PULLUP.

7. How to Use

Press the physical buttons.

The ESP32 sends the button states via Wi-Fi to the Python application.

The Python app simulates the corresponding keyboard presses on your PC.

You can play Blasphemous or other keyboard-compatible games.

8. Save and Reassign Keys

In the Python GUI, click Assign next to a button.

Press the key you want to assign.

Click Save Configuration to update config.json.

No manual editing of config.json is required.

9. Notes / Tips

Make sure your PC is connected to the same Wi-Fi as the ESP32.

Use a USB cable for debugging in Arduino IDE.

Test each button in the GUI before playing the game to ensure proper mapping.
