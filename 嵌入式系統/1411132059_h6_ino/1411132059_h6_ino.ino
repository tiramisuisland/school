
// String noteNames[] = {
//   "C2", "CS2", "D2", "DS2", "E2", "F2", "FS2", "G2", "GS2", "A2", "AS2", "B2",
//   "C3", "CS3", "D3", "DS3", "E3", "F3", "FS3", "G3", "GS3", "A3", "AS3", "B3",
//   "C4", "CS4", "D4", "DS4", "E4", "F4", "FS4", "G4", "GS4", "A4", "AS4", "B4",
//   "C5", "CS5", "D5", "DS5", "E5", "F5", "FS5", "G5", "GS5", "A5", "AS5", "B5",
//   "C6"
// };

// int noteFrequencies[] = {
//   65,   69,  73,  78,  82,  87,  93,  98, 104, 110, 117, 123,
//   131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247,
//   262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494,
//   523, 554, 587, 622, 659, 698, 740, 784, 830, 880, 932, 988,
//   1046
// };

#include <Arduino.h>
#define BUZZER_PIN A2  // Buzzer pin

// Define two melodies with frequency values
int S0[] = {
  196, 196, 220, 262, 294, 262, 294, 330,
  392, 330, 330, 294, 262, 294,
  330, 392, 392, 330, 392, 262, 294, 294,
  196, 330, 330, 294, 262,
  294, 294, 330, 294, 262, 220, 196, 220, 262,
  220, 262, 294, 330, 392,
  392, 392, 440, 392, 330, 294, 262, 220,
  196, 330, 330, 294, 262
};

int S0_D[] = {
  6, 2, 4, 4, 4, 2, 2, 8,
  6, 2, 2, 2, 4, 16,
  6, 2, 4, 2, 2, 6, 2, 8,
  6, 2, 4, 4, 16,
  6, 2, 4, 2, 2, 4, 2, 2, 8,
  6, 2, 4, 4, 16,
  6, 2, 4, 4, 4, 2, 2, 8,
  6, 2, 4, 4, 16
};

int S1[] = {
  784, 659, 659, 698, 587, 587,
  523, 587, 659, 698, 784, 784, 784,
  
  784, 659, 659, 698, 587, 587,
  523, 659, 784, 784, 659,
  
  587, 587, 587, 587, 587, 659, 698,
  659, 659, 659, 659, 659, 698, 784,
  
  784, 659, 659, 698, 587, 587,
  523, 659, 784, 784, 523,
};

int S1_D[] = {
  4, 4, 8, 4, 4, 8,
  4, 4, 4, 4, 4, 4, 8,
  
  4, 4, 8, 4, 4, 8,
  4, 4, 4, 4, 16,
  
  4, 4, 4, 4, 4, 4, 8,
  4, 4, 4, 4, 4, 4, 8,
  
  4, 4, 8, 4, 4, 8,
  4, 4, 4, 4, 16,
};

int S2[]{
  523, 523, 587, 659, 659,
  587, 523, 587, 659, 523,
  659, 659, 698, 784, 784,
  698, 659, 698, 784, 659,
  1046, 988, 880, 784,659,
  1046, 988, 880, 784,
  880,988, 1046, 784, 659,
  784, 698, 587, 523
  };

int S2_D[]{
  4,2,2,4,4,   2,2,2,2,8,
  4,2,2,4,4,   2,2,2,2,8,
  4,2,2,4,4,   4,2,2,8,
  4,2,2,4,4,   4,2,2,8,
};

// Function to play a song given melody and duration arrays
void playSong(int melody[], int noteDurations[], int length) {
  for (int thisNote = 0; thisNote < length; thisNote++) {
    int noteDuration = 100 * noteDurations[thisNote];
    int frequency = melody[thisNote];
    tone(BUZZER_PIN, frequency, noteDuration);
    int pauseBetweenNotes = noteDuration * 1.10;
    delay(pauseBetweenNotes);
    noTone(BUZZER_PIN);
  }
}

void setup() {
  // No initialization needed
}

void loop() {
  // Play S0 melody
  int Length = sizeof(S0) / sizeof(S0[0]);
  playSong(S0, S0_D, Length);
  
  delay(2000);  // Delay before the next melody
  
  // Play S1 melody
  Length = sizeof(S1) / sizeof(S1[0]);
  playSong(S1, S1_D, Length);
  
  delay(2000);
  Length = sizeof(S2) / sizeof(S2[0]);
  playSong(S2, S2_D, Length);
  
  delay(2000);  // Delay before repeating the loop
}
