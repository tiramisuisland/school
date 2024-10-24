#include <Arduino.h>
#define BUZZER_PIN A2  // 蜂鳴器的腳位
//小蜜蜂 蝴蝶 望春風
// 定義音符名稱和對應的頻率
String noteNames[] = {
  "C2", "CS2", "D2", "DS2", "E2", "F2", "FS2", "G2", "GS2", "A2", "AS2", "B2",
  "C3", "CS3", "D3", "DS3", "E3", "F3", "FS3", "G3", "GS3", "A3", "AS3", "B3",
  "C4", "CS4", "D4", "DS4", "E4", "F4", "FS4", "G4", "GS4", "A4", "AS4", "B4",
  "C5", "CS5", "D5", "DS5", "E5", "F5", "FS5", "G5", "GS5", "A5", "AS5", "B5",
  "C6"
};

int noteFrequencies[] = {
  65, 69, 73, 78, 82, 87, 93, 98, 104, 110, 117, 123,
  131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247,
  262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494,
  523, 554, 587, 622, 659, 698, 740, 784, 830, 880, 932, 988,
  1046
};

// 旋律部分使用音符名稱
String melody[] = {
  "C4", "C4", "G4", "G4", "A4", "A4", "G4",
  "F4", "F4", "E4", "E4", "D4", "D4", "C4",
  "G4", "G4", "F4", "F4", "E4", "E4", "D4",
  "G4", "G4", "F4", "F4", "E4", "E4", "D4",
  "C4", "C4", "G4", "G4", "A4", "A4", "G4",
  "F4", "F4", "E4", "E4", "D4", "D4", "C4",
};

// 每個音符的持續時間
int noteDurations[] = {
  4, 4, 4, 4, 4, 4, 2,
  4, 4, 4, 4, 4, 4, 2,
  4, 4, 4, 4, 4, 4, 2,
  4, 4, 4, 4, 4, 4, 2,
  4, 4, 4, 4, 4, 4, 2,
  4, 4, 4, 4, 4, 4, 2 
};


// 查找音符名稱並返回對應的頻率
int getNoteFrequency(String note) {
  for (int i = 0; i < sizeof(noteNames) / sizeof(noteNames[0]); i++) {
    if (noteNames[i] == note) {
      return noteFrequencies[i];
    }
  }
  return 0;  // 如果未找到音符，返回 0
}

void setup() {
  // 不需要額外初始化
}

void loop() {
  // 播放每個音符
  for (int thisNote = 0; thisNote < 32; thisNote++) {
    int noteDuration = 1000 / noteDurations[thisNote];
    
    // 查找對應音符的頻率
    int frequency = getNoteFrequency(melody[thisNote]);

    // 播放對應頻率的音符
    tone(BUZZER_PIN, frequency, noteDuration);

    // 播放後暫停一會兒
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);

    // 停止音符
    noTone(BUZZER_PIN);
  }

  // 完成演奏後延遲一段時間再重複
  delay(2000);
}
