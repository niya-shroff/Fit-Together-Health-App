#define USE_ARDUINO_INTERRUPTS true 
#define PULSEPIN A0 
#include <PulseSensorPlayground.h>

PulseSensorPlayground pulseSensor;

void setup() {
  Serial.begin(9600);
  int threshold = 550;
  pulseSensor.begin();
  pulseSensor.setThreshold(threshold);
  pulseSensor.analogInput(0);

}

int BPM_min[500];
int count = 0;
void loop() {
  if (pulseSensor.sawStartOfBeat()) {
    int timeFirst = millis();
    int timeSecond;
    
    float pulseVal = analogRead(PULSEPIN);
    Serial.print("Pulse: ");
    Serial.println(pulseVal);
    int BPM = pulseSensor.getBeatsPerMinute();
    Serial.print("BPM: ");
    Serial.println(BPM);
    BPM_min[count] = BPM;
    count+=1;

    timeSecond = millis();
    if (timeSecond >= timeFirst + 60000) {
      Serial.println("Hello"); //test if this loop ever runs
      float BPM_min_avg;
    
      for (int i=0; i < count; i++) {
        BPM_min_avg += BPM_min[i];
      }
      
      BPM_min_avg = BPM_min_avg / (count+1);
      Serial.println(BPM_min_avg);
      count = 0;
    }
    
  }
}
  
