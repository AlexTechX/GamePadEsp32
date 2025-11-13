<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>GamePad ESP32 – User Guide</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      background-color: #f5f5f5;
      padding: 20px;
      color: #333;
    }
    h1, h2, h3 {
      color: #1a73e8;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 15px 0;
      background-color: #fff;
    }
    table, th, td {
      border: 1px solid #ccc;
    }
    th, td {
      padding: 10px;
      text-align: center;
    }
    th {
      background-color: #1a73e8;
      color: #fff;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
    .note {
      background-color: #fff3cd;
      border-left: 5px solid #ffeeba;
      padding: 10px;
      margin: 10px 0;
    }
    code {
      background-color: #eee;
      padding: 2px 4px;
      border-radius: 4px;
    }
  </style>
</head>
<body>

<h1>🎮 GamePad ESP32 – User Guide</h1>

<h2>1. Project Description</h2>
<p>This project is a <strong>wireless controller based on the ESP32</strong> to play <em>Blasphemous</em> or other keyboard-controlled games.  
It uses <strong>14 physical buttons</strong> and communicates via <strong>Wi-Fi</strong> with a Python application that converts button signals into configurable keyboard inputs.</p>

<h2>2. Requirements</h2>
<h3>Hardware</h3>
<ul>
  <li>ESP32 (38 pins)</li>
  <li>14 push buttons</li>
  <li>Wires and breadboard (optional)</li>
</ul>
<h3>Software</h3>
<ul>
  <li>Arduino IDE (to upload the <code>.ino</code> file)</li>
  <li>Python 3.12+</li>
  <li>Python libraries: <code>pynput</code>, <code>websocket-client</code></li>
  <li>Local Wi-Fi connection</li>
</ul>

<h2>3. Download the Project</h2>
<ol>
  <li>Open Git Bash, CMD, or PowerShell.</li>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/AlexTechX/GamePadEsp32.git</code></pre>
  </li>
  <li>Navigate into the project folder:
    <pre><code>cd GamePadEsp32</code></pre>
  </li>
</ol>

<h2>4. Configure and Run the Python Application</h2>
<ol>
  <li>Install required Python libraries:
    <pre><code>pip install pynput websocket-client</code></pre>
  </li>
  <li>Connect to the ESP32 Wi-Fi network.</li>
  <li>Run the Python script:
    <pre><code>python mando_blasphemous.py</code></pre>
  </li>
  <li>The <strong>graphical interface</strong> will open to:
    <ul>
      <li>Assign keys to each button</li>
      <li>Save the configuration to <code>config.json</code></li>
    </ul>
  </li>
</ol>
<div class="note">Note: Special keys like <code>space</code>, <code>enter</code>, <code>shift</code>, etc., are automatically interpreted.</div>

<h2>5. Upload the Arduino Sketch to the ESP32</h2>
<ol>
  <li>Open Arduino IDE and load <code>Gamepad.ino</code>.</li>
  <li>Select:
    <ul>
      <li><strong>Board → ESP32</strong></li>
      <li><strong>COM port → your ESP32 port</strong></li>
    </ul>
  </li>
  <li>Click <strong>Upload</strong>.</li>
  <li>Open the <strong>Serial Monitor</strong> to check the ESP32 IP (e.g., <code>192.168.4.1</code>).</li>
</ol>

<h2>6. Wiring Guide</h2>
<p>Connect each button between the assigned <strong>ESP32 GPIO pin</strong> and <strong>GND</strong>.</p>

<table>
  <tr>
    <th>Function</th>
    <th>GPIO</th>
    <th>Default Key</th>
  </tr>
  <tr><td>UP</td><td>32</td><td>w</td></tr>
  <tr><td>DOWN</td><td>33</td><td>s</td></tr>
  <tr><td>LEFT</td><td>12</td><td>a</td></tr>
  <tr><td>RIGHT</td><td>26</td><td>d</td></tr>
  <tr><td>ATTACK</td><td>25</td><td>k</td></tr>
  <tr><td>DASH</td><td>27</td><td>l</td></tr>
  <tr><td>PRAYER</td><td>13</td><td>j</td></tr>
  <tr><td>USE_VESSEL</td><td>14</td><td>f</td></tr>
  <tr><td>JUMP</td><td>4</td><td>space</td></tr>
  <tr><td>START</td><td>16</td><td>enter</td></tr>
  <tr><td>SELECT</td><td>17</td><td>shift</td></tr>
  <tr><td>ITEM1</td><td>5</td><td>q</td></tr>
  <tr><td>ITEM2</td><td>18</td><td>e</td></tr>
  <tr><td>ESC</td><td>19</td><td>esc</td></tr>
</table>

<div class="note">
Notes: <br>
- One terminal of the button → assigned GPIO<br>
- Other terminal → GND<br>
- No external resistor is needed; code uses <code>INPUT_PULLUP</code>.
</div>

<h2>7. How to Use</h2>
<ol>
  <li>Press the physical buttons.</li>
  <li>The ESP32 sends button states via Wi-Fi to the Python application.</li>
  <li>The Python app simulates the corresponding keyboard presses on your PC.</li>
  <li>You can play <em>Blasphemous</em> or other keyboard-compatible games.</li>
</ol>

<h2>8. Save and Reassign Keys</h2>
<ul>
  <li>In the Python GUI, click <strong>Assign</strong> next to a button.</li>
  <li>Press the key you want to assign.</li>
  <li>Click <strong>Save Configuration</strong> to update <code>config.json</code>.</li>
  <li>No manual editing of <code>config.json</code> is required.</li>
</ul>

<h2>9. Tips</h2>
<ul>
  <li>Ensure your PC is connected to the same Wi-Fi as the ESP32.</li>
  <li>Use a USB cable for debugging in Arduino IDE.</li>
  <li>Test each button in the GUI before starting the game.</li>
</ul>

</body>
</html>
