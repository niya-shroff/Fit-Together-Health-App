// makes a good, legible graph of the pulse
// CANNOT implement any pulseSensorPlayground functions other than threshold and analog 

#define PULSEPIN A0 
#include <PulseSensorPlayground.h>

PulseSensorPlayground pulseSensor;

void setup() {
  Serial.begin(9600);
  int threshold = 550;
  pulseSensor.setThreshold(threshold);

}

int count = 0;
void loop() {
    float pulseVal = analogRead(PULSEPIN);
    Serial.print("Pulse: ");
    Serial.println(pulseVal);
    
  }

  
