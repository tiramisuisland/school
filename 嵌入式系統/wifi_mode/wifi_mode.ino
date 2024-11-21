#include <WiFi.h>
#include <WebSocketsServer.h>
#include <DHT.h>

// Wi-Fi 資訊
const char* ssid = "tiramisu";
const char* password = "0905348451";

// DHT11
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// LED
#define LED_PIN 2
bool ledState = false;

// 超音波模組
#define TRIG_PIN 5
#define ECHO_PIN 18

// WebSocket Server
WebSocketsServer webSocket(81);

// HTTP Server
WiFiServer server(80);

// 網頁 HTML
const char HTML_PAGE[] PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DHT 11 LED</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin-top: 50px;
    }
    .button {
      display: inline-block;
      padding: 10px 20px;
      margin: 10px;
      font-size: 16px;
      cursor: pointer;
      border-radius: 5px;
      border: none;
    }
    .on {
      background-color: green;
      color: white;
    }
    .off {
      background-color: red;
      color: white;
    }
  </style>
  <script>
    let socket;
    function initWebSocket() {
      socket = new WebSocket(`ws://${location.hostname}:81/`);
      socket.onmessage = function(event) {
        const data = event.data.split(",");
        document.getElementById("temperature").innerText = data[0].split(":")[1] + " °C";
        document.getElementById("humidity").innerText = data[1].split(":")[1] + " %";
        document.getElementById("distance").innerText = data[2].split(":")[1] + " cm";
      };
    }
    function ledOn() {
      socket.send("LED_ON");
    }
    function ledOff() {
      socket.send("LED_OFF");
    }
    window.onload = initWebSocket;
  </script>
</head>
<body>
  <h1>DHT 11 LED</h1>
  <p>Temperature: <span id="temperature">--</span></p>
  <p>Humidity: <span id="humidity">--</span></p>
  <p>Distance: <span id="distance">--</span></p>
  <button class="button on" onclick="ledOn()">LED On</button>
  <button class="button off" onclick="ledOff()">LED Off</button>
</body>
</html>
)rawliteral";

void handleWebSocketMessage(uint8_t num, uint8_t *payload, size_t length) {
  String message = (char*)payload;
  if (message == "LED_ON") {
    ledState = true;
    digitalWrite(LED_PIN, HIGH);
  } else if (message == "LED_OFF") {
    ledState = false;
    digitalWrite(LED_PIN, LOW);
  }
}

void webSocketEvent(uint8_t num, WStype_t type, uint8_t *payload, size_t length) {
  if (type == WStype_TEXT) {
    handleWebSocketMessage(num, payload, length);
  }
}

// 測量超音波距離
float measureDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH);
  return duration * 0.034 / 2.0; // 計算距離（單位：cm）
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected.");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  dht.begin();
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  webSocket.begin();
  webSocket.onEvent(webSocketEvent);

  server.begin();
}

void loop() {
  webSocket.loop();

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  float distance = measureDistance();

  if (isnan(temperature) || isnan(humidity)) {
    temperature = 0.0;
    humidity = 0.0;
  }

  String data = String("TEMP:") + temperature +
                ",HUMID:" + humidity +
                ",DIST:" + distance;
  webSocket.broadcastTXT(data);

  WiFiClient client = server.available();
  if (client) {
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("Connection: close");
    client.println();
    client.println(HTML_PAGE);
    client.stop();
  }

  delay(100); // 每秒更新
}
