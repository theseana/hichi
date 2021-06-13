from time import sleep
import serial


ser = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=9600,
)


while True:
    ser.write(bytes('1', 'utf-8'))
    sleep(2)
    ser.write(bytes('0', 'utf-8'))
    sleep(2)

