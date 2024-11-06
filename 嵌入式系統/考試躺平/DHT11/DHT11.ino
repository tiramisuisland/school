#include "DHT.h"

#define DHTPIN 8      // DHT11 数据引脚连接到 Arduino 的数字引脚 2
#define DHTTYPE DHT11 // 定义使用的传感器类型为 DHT11

DHT dht(DHTPIN, DHTTYPE); // 初始化 DHT 传感器

void setup() {
  Serial.begin(9600); 
  dht.begin();        // 启动 DHT 传感器
}

void loop() {
  delay(2000);        // 等待 2 秒（DHT11 采样频率不能太高）

  float humidity = dht.readHumidity();          // 读取湿度
  float temperature = dht.readTemperature();    // 读取摄氏温度

  // 检查读取是否成功
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("读取失败，请检查传感器连接！");
    return;
  }

  // 显示结果
  Serial.print("湿度: ");
  Serial.print(humidity);
  Serial.print(" %\t");
  Serial.print("温度: ");
  Serial.print(temperature);
  Serial.println(" *C");
}
