#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

byte SB[3][8] = {
  {B00000,B10001,B00000,B00000,B10001,B01110,B00000},
  {B00000,B10001,B00000,B00000,B01110,B10001,B00000},
  {B00000,B01010,B11111,B11111,B01110,B00100,B00000},
  };

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("s1411132059");
  for(byte i=0 ;i<3;i++){
    lcd.createChar(i,SB[i]);
  }
}

void loop(){
  for (byte i=0; i<3;i++){
    lcd.setCursor(0,1);
    lcd.write(byte(i));
    delay(1000);
  }
}
