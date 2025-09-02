# MicroPython I2C Scanner Example
from machine import Pin, SoftI2C

# Choose your desired I2C pins (SCL, SDA)
# For example, use GPIO 5 for SCL and GPIO 4 for SDA
i2c = SoftI2C(scl=Pin(9), sda=Pin(8)) 

print('I2C Scanner')
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C devices found!")
else:
    print('I2C devices found:', len(devices))
    for device in devices:
        print("I2C address (hex):", hex(device))