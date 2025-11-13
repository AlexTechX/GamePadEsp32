<h1 style="color:#1a73e8;">🎮 GamePad ESP32 – User Guide</h1>

<h2 style="color:#1a73e8;">1️⃣ Project Description</h2>
<p>This project is a <strong>wireless controller based on the ESP32</strong> for playing <em>Blasphemous</em> or other keyboard-controlled games.</p>
<p>It uses <strong>14 physical buttons</strong> and communicates via <strong>Wi-Fi</strong> with a Python application that converts button signals into configurable keyboard inputs.</p>

<h2 style="color:#1a73e8;">2️⃣ Requirements</h2>
<h3>Hardware</h3>
<ul>
  <li>ESP32 (38 pins)</li>
  <li>14 push buttons</li>
  <li>Wires and breadboard (optional)</li>
</ul>
<h3>Software</h3>
<ul>
  <li>Arduino IDE (to upload <code>Gamepad.ino</code>)</li>
  <li>Python 3.12+</li>
  <li>Python libraries: <code>pynput</code>, <code>websocket-client</code></li>
  <li>Local Wi-Fi connection</li>
</ul>

<h2 style="color:#1a73e8;">3️⃣ Download the Project</h2>
<pre style="background:#eee;padding:10px;border-radius:5px;">
git clone https://github.com/AlexTechX/GamePadEsp32.git
cd GamePadEsp32
</pre>

<h2 style="color:#1a73e8;">4️⃣ Configure and Run the Python Application</h2>
<pre style="background:#eee;padding:10px;border-radius:5px;">
pip install pynput websocket-client
python mando_blasphemous.py
</pre>
<p>The GUI will open where you can:</p>
<ul>
  <li>Assign keys to each button</li>
  <li>Save the configuration to <code>config.json</code></li>
</ul>
<p style="background:#fff3cd;border-left:5px solid #ffeeba;padding:10px;">Note: Special keys like <code>space</code>, <code>enter</code>, <code>shift</code> are automatically interpreted.</p>

<h2 style="color:#1a73e8;">5️⃣ Upload the Arduino Sketch</h2>
<ol>
  <li>Open Arduino IDE and load <code>Gamepad.ino</code>.</li>
  <li>Select Board → ESP32, and COM port → your ESP32 port.</li>
  <li>Click <strong>Upload</strong>.</li>
  <li>Open Serial Monitor to check ESP32 IP (e.g., <code>192.168.4.1</code>).</li>
</ol>

<h2 style="color:#1a73e8;">6️⃣ Wiring Guide</h2>
<p>Connect each button between the assigned <strong>ESP32 GPIO pin</strong> and <strong>GND</strong>.</p>

<table style="width:100%;border-collapse:collapse;">
  <tr style="background:#1a73e8;color:white;">
    <th style="padding:10px;border:1px solid #ccc;">Function</th>
    <th style="padding:10px;border:1px solid #ccc;">GPIO</th>
    <th style="padding:10px;border:1px solid #ccc;">Default Key</th>
  </tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">UP</td><td style="padding:10px;border:1px solid #ccc;">32</td><td style="padding:10px;border:1px solid #ccc;">w</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">DOWN</td><td style="padding:10px;border:1px solid #ccc;">33</td><td style="padding:10px;border:1px solid #ccc;">s</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">LEFT</td><td style="padding:10px;border:1px solid #ccc;">12</td><td style="padding:10px;border:1px solid #ccc;">a</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">RIGHT</td><td style="padding:10px;border:1px solid #ccc;">26</td><td style="padding:10px;border:1px solid #ccc;">d</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">ATTACK</td><td style="padding:10px;border:1px solid #ccc;">25</td><td style="padding:10px;border:1px solid #ccc;">k</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">DASH</td><td style="padding:10px;border:1px solid #ccc;">27</td><td style="padding:10px;border:1px solid #ccc;">l</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">PRAYER</td><td style="padding:10px;border:1px solid #ccc;">13</td><td style="padding:10px;border:1px solid #ccc;">j</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">USE_VESSEL</td><td style="padding:10px;border:1px solid #ccc;">14</td><td style="padding:10px;border:1px solid #ccc;">f</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">JUMP</td><td style="padding:10px;border:1px solid #ccc;">4</td><td style="padding:10px;border:1px solid #ccc;">space</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">START</td><td style="padding:10px;border:1px solid #ccc;">16</td><td style="padding:10px;border:1px solid #ccc;">enter</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">SELECT</td><td style="padding:10px;border:1px solid #ccc;">17</td><td style="padding:10px;border:1px solid #ccc;">shift</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">ITEM1</td><td style="padding:10px;border:1px solid #ccc;">5</td><td style="padding:10px;border:1px solid #ccc;">q</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">ITEM2</td><td style="padding:10px;border:1px solid #ccc;">18</td><td style="padding:10px;border:1px solid #ccc;">e</td></tr>
  <tr><td style="padding:10px;border:1px solid #ccc;">ESC</td><td style="padding:10px;border:1px solid #ccc;">19</td><td style="padding:10px;border:1px solid #ccc;">esc</td></tr>
</table>

<p style="background:#fff3cd;border-left:5px solid #ffeeba;padding:10px;">Notes: One terminal of the button → assigned GPIO, Other terminal → GND. No external resistor needed; code uses INPUT_PULLUP.</p>

<h2 style="color:#1a73e8;">7️⃣ How to Use</h2>
<ol>
  <li>Press the physical buttons.</li>
  <li>ESP32 sends button states via Wi-Fi to Python app.</li>
  <li>Python app simulates keyboard presses on PC.</li>
  <li>Play Blasphemous or any keyboard-compatible game.</li>
</ol>
