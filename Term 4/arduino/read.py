from os import initgroups
import serial


ser = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=9600,
)
fresh = ""
res = [0, 0, 0, 0, 0]
while True:
    input_value = ser.read().decode().replace("\r", "*").replace("\n", " ")
    # if input_value.isdigit():
    #     if input_value == '1':
    #         print("ON")
    #     else:
    #         print("OFF")
    if input_value != "*":
        fresh += input_value
        if input_value == " ":
            res.append(float(fresh.strip()))
            res.pop(0)
            print(res, end="   ")
            print(sum(res)/len(res))
            fresh = ""
