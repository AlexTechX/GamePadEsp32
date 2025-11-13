import json
import threading
import websocket
from pynput.keyboard import Controller, Key
import tkinter as tk
from tkinter import messagebox

# Interfaz entre nombre en config y objeto que presiona pynput
SPECIAL_KEYS = {
    "space": Key.space,
    "enter": Key.enter,
    "shift": Key.shift,
    "ctrl": Key.ctrl,
    "alt": Key.alt,
    "tab": Key.tab,
    "esc": Key.esc,
    "backspace": Key.backspace,
    "up": Key.up,
    "down": Key.down,
    "left": Key.left,
    "right": Key.right,
}

# Archivo de configuración
CONFIG_FILE = "config.json"

# Lista de botones esperados desde el ESP32
button_names = [
    "UP", "DOWN", "LEFT", "RIGHT",
    "ATTACK", "DASH", "PRAYER", "USE_VESSEL",
    "JUMP", "START", "SELECT",
    "ITEM1", "ITEM2", "ITEM3"
]

# Carga segura del archivo config.json
def load_config():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Asegurar que todas las keys existan; si falta, poner por defecto
            defaults = default_map()
            for k, v in defaults.items():
                if k not in data or not isinstance(data[k], str) or data[k] == "":
                    data[k] = v
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return default_map()

# Valores por defecto (si no existe config.json o está corrupto)
def default_map():
    return {
        "UP": "w", "DOWN": "s", "LEFT": "a", "RIGHT": "d",
        "ATTACK": "k", "DASH": "l", "PRAYER": "j", "USE_VESSEL": "f",
        "JUMP": "space", "START": "enter", "SELECT": "shift",
        "ITEM1": "q", "ITEM2": "e", "ITEM3": "r"
    }

# Resuelve la cadena guardada en config a un objeto que pynput acepte
def resolve_key(key_str):
    if not isinstance(key_str, str):
        return key_str
    low = key_str.lower()
    if low in SPECIAL_KEYS:
        return SPECIAL_KEYS[low]
    # Si es una cadena de longitud 1, devolverla tal cual (tecla normal)
    if len(key_str) == 1:
        return key_str
    # Para keysymes como "comma" o "semicolon" devolver la misma cadena
    # pynput aceptará muchos strings (la librería traducirá)
    return key_str

# Guardar configuración (siempre como cadenas)
def save_config_file(mapping):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)

# Inicializar
key_map = load_config()
pressed = {k: False for k in button_names}
keyboard = Controller()

# Maneja mensajes entrantes del ESP32
def on_message(ws, message):
    try:
        data = json.loads(message)
    except Exception:
        return
    for btn, val in data.items():
        if btn not in key_map:
            continue
        key_cfg = key_map[btn]
        key_obj = resolve_key(key_cfg)
        # Presiona o libera la tecla según el estado recibido (1 = presionado)
        try:
            if val == 1 and not pressed.get(btn, False):
                keyboard.press(key_obj)
                pressed[btn] = True
            elif val == 0 and pressed.get(btn, False):
                keyboard.release(key_obj)
                pressed[btn] = False
        except Exception:
            # En caso de que pynput no acepte el objeto, ignorar el error
            pass

def run_client():
    # Mantiene reconexión automática
    while True:
        try:
            ws = websocket.WebSocketApp("ws://192.168.4.1:81/",
                                        on_message=on_message)
            ws.run_forever()
        except Exception:
            import time
            time.sleep(2)

# GUI: asignar teclas y guardar
root = tk.Tk()
root.title("Configuración mando Blasphemous")

entries = {}

def open_assign_window(button_name):
    def on_key(event):
        keysym = event.keysym
        # For special keys like 'space', 'Return' convert to our naming
        mapping_keysym = {
            "space": "space",
            "Return": "enter",
            "Shift_L": "shift",
            "Shift_R": "shift",
            "Control_L": "ctrl",
            "Control_R": "ctrl",
            "Alt_L": "alt",
            "Alt_R": "alt",
            "Tab": "tab",
            "Escape": "esc",
            "BackSpace": "backspace",
            "Up": "up",
            "Down": "down",
            "Left": "left",
            "Right": "right"
        }
        name = mapping_keysym.get(keysym, keysym.lower() if len(keysym) == 1 else keysym.lower())
        key_map[button_name] = name
        entries[button_name].delete(0, tk.END)
        entries[button_name].insert(0, name)
        assign_win.destroy()

    assign_win = tk.Toplevel(root)
    assign_win.title(f"Asigar tecla - {button_name}")
    tk.Label(assign_win, text="Presione una tecla...").pack(padx=20, pady=10)
    assign_win.bind("<Key>", on_key)
    assign_win.focus_set()

def save_and_notify():
    save_config_file(key_map)
    messagebox.showinfo("Guardar", "Configuración guardada en config.json")

# Construir interfaz
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

for i, name in enumerate(button_names):
    tk.Label(frame, text=name, width=12, anchor="w").grid(row=i, column=0, padx=5, pady=4)
    ent = tk.Entry(frame, width=15)
    ent.grid(row=i, column=1, padx=5)
    ent.insert(0, key_map.get(name, ""))
    entries[name] = ent
    tk.Button(frame, text="Asignar", command=lambda n=name: open_assign_window(n)).grid(row=i, column=2, padx=5)

tk.Button(root, text="Guardar configuración", command=save_and_notify).pack(pady=8)

# Iniciar hilo WebSocket y luego GUI
threading.Thread(target=run_client, daemon=True).start()

root.mainloop()
