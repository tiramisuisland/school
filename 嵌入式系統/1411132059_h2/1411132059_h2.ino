void setup() {
  for(int i=2;i<=5;i++){
    pinMode(i,INPUT_PULLUP);
    pinMode(i+8,OUTPUT);
  }
}
void loop() {
  if(digitalRead(5)==0){
    LED(0,0,1,20);
    for(int i=0;i<=2;i++){
    LED(0,1,0,5);
    delay(500);
    }
    LED(1,0,0,30);
  }
  if(digitalRead(2)==0){
    LED(1,0,0,10);
    LED(0,1,0,10);
    LED(0,0,1,10);
  }
  if(digitalRead(3)==0){
    LED(0,0,1,10);
    LED(0,1,0,10);
    LED(1,0,0,10);
  }
  if(digitalRead(4)==0){
    LED(1,0,0,10);
    LED(0,1,0,10);
    LED(0,0,1,10);
    LED(0,1,0,10);
  }
}
void LED(int a,int b,int c,int d){
  digitalWrite(12,a);
  digitalWrite(11,b);
  digitalWrite(10,c);
  delay(100*d);
  for (int i = 10; i <= 12; i++)digitalWrite(i, 0);
}