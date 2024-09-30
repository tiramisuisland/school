void setup() {
  for(int i=2;i<=4;i++){
    pinMode(i,INPUT_PULLUP);
    pinMode(i+8,OUTPUT);
  }
}
void loop() {
  for(int i=0; i<=2; i++) {
    digitalWrite(10+i, digitalRead(2+i));
  }
}