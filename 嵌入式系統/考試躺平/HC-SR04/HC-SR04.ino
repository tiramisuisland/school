const int trigPin = 9;    // Trig 引脚
const int echoPin = 10;   // Echo 引脚

void setup() {
  Serial.begin(9600);     // 初始化串口通信
  pinMode(trigPin, OUTPUT); // 设置 Trig 为输出
  pinMode(echoPin, INPUT);  // 设置 Echo 为输入
}

void loop() {
  long duration;
  float distance;

  // 清除 Trig 引脚
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // 触发超声波发送
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // 读取 Echo 引脚，返回声音波的往返时间
  duration = pulseIn(echoPin, HIGH);

  // 计算距离（单位：厘米）
  distance = duration * 0.034 / 2;

  // 在串口监视器输出距离
  Serial.print("距离: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(500); // 延迟 500 毫秒
}
