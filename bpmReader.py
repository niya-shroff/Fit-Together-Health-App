import serial
ardruino = serial.Serial('/dev/cu.usbserial-02328966', timeout=1, baudrate=9600)

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