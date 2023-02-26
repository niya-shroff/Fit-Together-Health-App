import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial

#initialize serial port
ser = serial.Serial()
ser.port = '/dev/cu.usbserial-02328966' #Arduino serial port
ser.baudrate = 9600
ser.timeout = 10 #specify timeout when using readline()
ser.open()
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters

# Create figure for plotting
fig = plt.figure()

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    #Aquire and parse data from serial port
    line=ser.readline()
    line_as_list = line.split(b',')
    i = int(line_as_list[0])
    BPM = line_as_list[1]
    relProb_as_list = BPM.split(b'\n')
    relProb_float = float(relProb_as_list[0])

animate(10, 10, 10)
