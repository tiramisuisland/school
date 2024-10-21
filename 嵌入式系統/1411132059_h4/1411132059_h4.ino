#include <DHT.h>
#define TRIG_PIN 6
#define ECHO_PIN 7
#define LED_PIN 10
#define DHT_PIN 8
#define DHT_TYPE DHT11
DHT dht(DHT_PIN, DHT_TYPE);
void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // 測量距離
  long duration, distance;
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2;  // 距離計算公式

  // 判斷距離是否小於 10 cm
  if (distance < 10) {
    digitalWrite(LED_PIN, HIGH);  // LED 亮

    // 讀取溫濕度
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    // 顯示溫度與濕度
    if (isnan(temperature) || isnan(humidity)) {
      Serial.println("讀取溫濕度錯誤！");
    } else {
      Serial.print("溫度: ");
      Serial.print(temperature);
      Serial.print(" °C ");
      Serial.print("濕度: ");
      Serial.print(humidity);
      Serial.println(" %");
    }
  } else {
    digitalWrite(LED_PIN, LOW);  // LED 熄滅
  }

  // 延遲 1 秒
  delay(100);
}
