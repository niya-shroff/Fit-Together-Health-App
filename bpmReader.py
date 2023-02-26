from time import sleep

import pandas as pd
import serial
from openpyxl.reader.excel import ExcelReader
from pandas import ExcelWriter

ardruino = serial.Serial('/dev/cu.usbserial-02328966', timeout=1, baudrate=9600)

bpmData = []
count = 0

# We would actually keep count < a high number that way we can get a more accurage BPM reading
while count < 5:
    input = str(ardruino.readline())
    input = input.split('b')[1].split('\\')[0].split("'")[1]
    if (input != "" and input != "exit setupInterrupts"):
        print(input)
        bpmData.append(input)
        count += 1


df = pd.DataFrame([[bpmData]], columns=["BPM"])
with ExcelWriter("bpm.xlsx") as writer:
    df.to_excel(writer)
