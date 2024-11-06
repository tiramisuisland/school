#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// 初始化 LiquidCrystal_I2C 物件，參數是 LCD 的 I2C 地址和尺寸 (16x2)
LiquidCrystal_I2C lcd(0x27, 16, 2); // 請確認 I2C 地址，通常為 0x27 或 0x3F

void setup() {
  lcd.init();           // 初始化 LCD
  lcd.clear(); // 清除 LCD 上的所有文字
  lcd.backlight();      // 開啟背光

  // 設定顯示文字
  lcd.setCursor(0, 0);  // 左上角 (0,0)
  lcd.print("Hello, World!");
  lcd.setCursor(0, 1);  // 第二行 (0,1)
  lcd.print("Arduino LCD I2C");

  
}

void loop() {
  // 這裡可以加入您的其他程式邏輯
}
