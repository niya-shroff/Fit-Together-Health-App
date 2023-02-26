import serial
try:
    # follow this website: https://www.instructables.com/Sending-Data-From-Arduino-to-Python-Via-USB/
    ardruino = serial.Serial('/ArduinoReader', timeout=1)
except:
    print("Please check the port")
bpmData = []
count = 0
while count < 60:
    bpmData.append(str(ardruino.readline()))
    count += 1

def writeBPM(bpmData):
    bpmCSV = open("data/bpm.csv", mode='w')
    for i in range(len(bpmData)):
        bpmCSV.write(bpmData[i] + '\n')
    bpmCSV.close()

writeBPM(bpmData)