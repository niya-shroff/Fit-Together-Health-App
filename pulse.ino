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
int timeFirst = millis();
int timeSecond;
void loop() {
  if (pulseSensor.sawStartOfBeat()) {
    
    float pulseVal = analogRead(PULSEPIN);
    /*Serial.print("Pulse: ");
    Serial.println(pulseVal);*/
    //int BPM = pulseSensor.getBeatsPerMinute();
    /*Serial.print("BPM: ");
    Serial.println(BPM);
    BPM_min[count] = BPM;
    count+=1;*/

    timeSecond = millis();
    if (timeSecond >= timeFirst + 6000) {
      Serial.println(pulseSensor.getBeatsPerMinute());
      timeFirst = timeSecond;
    }
    
  }
}
  
