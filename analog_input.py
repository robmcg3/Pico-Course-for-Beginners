from machine import Pin, ADC # we need to import ADC to use analog inputs
import time
# updated for RP2040 zero

# set up pin 26 as an analog input
pot = ADC(Pin(26)) 

# constant to convert the 0 - 65535 range to 0 - 3.3 volts
conversion_factor = 3.3 / 65535

while True:
    # read analog input and store it in a variable called pot_voltage
    pot_voltage = pot.read_u16()
  
    # print pot_voltage
    print(pot_voltage)
    time.sleep(0.1)