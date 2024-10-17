	// 光敏電阻控制LED亮或熄 並顯示光敏電阻輸出值與LED狀態
int s=0,LED_state=0;
void setup() {
  Serial.begin(9600);
  pinMode(A5,INPUT_PULLUP);
  pinMode(10,OUTPUT);
}

void loop() {
  Serial.print("A5: ");
  s = analogRead(A5);
  Serial.print(s);

  if(s>100) {
    digitalWrite(10,0);
    LED_state=0;
  }
  else {
    digitalWrite(10,1);
    LED_state=1;
  }
  Serial.print("LED_state: ");
  Serial.println(LED_state);
}
