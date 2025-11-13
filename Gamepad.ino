#include <WiFi.h>
#include <WebSocketsServer.h>
#include <ArduinoJson.h>

// Configuración de la red Wi-Fi que crea el ESP32
const char* ssid = "ESP32_Blasphemous";
const char* password = "12345678";

// Servidor WebSocket en el puerto 81
WebSocketsServer webSocket = WebSocketsServer(81);

// Cantidad total de botones
const int NUM_BUTTONS = 14;

// Asignación de pines GPIO a cada acción
const int buttons[NUM_BUTTONS] = {
  32, 33, 25, 26, 27, 12, 13, 14, 4, 16, 17, 5, 18, 19
};

// Nombres identificadores de cada botón
const char* buttonNames[NUM_BUTTONS] = {
  "UP", "DOWN", "LEFT", "RIGHT",
  "ATTACK", "DASH", "PRAYER", "USE_VESSEL",
  "JUMP", "START", "SELECT",
  "ITEM1", "ITEM2", "ITEM3"
};

// Estado anterior de cada botón para detectar cambios
int lastState[NUM_BUTTONS];

void setup() {
  Serial.begin(115200);
  Serial.println("\n[ESP32] Inicializando mando Blasphemous...");

  // Configura cada pin como entrada con resistencia pull-up
  for (int i = 0; i < NUM_BUTTONS; i++) {
    pinMode(buttons[i], INPUT_PULLUP);
    lastState[i] = !digitalRead(buttons[i]);
  }

  // Crea la red Wi-Fi del mando
  WiFi.softAP(ssid, password);
  Serial.print("[WiFi] Red creada: ");
  Serial.println(ssid);
  Serial.print("[WiFi] IP: ");
  Serial.println(WiFi.softAPIP());

  // Inicia el servidor WebSocket
  webSocket.begin();
  Serial.println("[WebSocket] Servidor iniciado en puerto 81");
}

void loop() {
  webSocket.loop();
  StaticJsonDocument<512> doc;
  bool changed = false;

  // Lectura de los estados de los botones
  for (int i = 0; i < NUM_BUTTONS; i++) {
    int reading = !digitalRead(buttons[i]); // Activo en bajo
    doc[buttonNames[i]] = reading;

    // Detecta si el botón cambió de estado
    if (reading != lastState[i]) {
      Serial.print(buttonNames[i]);
      Serial.print(" -> ");
      Serial.println(reading ? "PRESIONADO" : "SUELTO");
      lastState[i] = reading;
      changed = true;
    }
  }

  // Envía solo si hubo un cambio
  if (changed) {
    String jsonStr;
    serializeJson(doc, jsonStr);
    webSocket.broadcastTXT(jsonStr);
  }

  delay(15); // Controla la frecuencia de actualización (~60 Hz)
}
