#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#define TRIG_PIN 6
#define ECHO_PIN 7
#define LED_PIN 13
#define DHT_PIN 8
#define DHT_TYPE DHT11
DHT dht(DHT_PIN, DHT_TYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  
  dht.begin();
  lcd.init(); 
  lcd.backlight();
  lcd.setCursor(0, 0);  // 移動到第一行第一列
  lcd.print("s1411132059");
  lcd.setCursor(0, 1);
  lcd.print("Hello Arduino!");
  delay(1000);
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
      lcd.setCursor(0, 0);
      lcd.print("Sensor Error    ");
    } else {
      Serial.print("溫度: ");
      Serial.print(temperature);
      Serial.print(" °C ");
      Serial.print("濕度: ");
      Serial.print(humidity);
      Serial.println(" %");
      
      lcd.setCursor(0, 1);
      lcd.print("T:");
      lcd.print(temperature);
      lcd.print("C:");
      
      lcd.setCursor(8, 1);
      lcd.print("H:");
      lcd.print(humidity);
      lcd.print("%  ");
    }
  } else {
    digitalWrite(LED_PIN, LOW);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Waiting...");
  }

  delay(1000);
}
