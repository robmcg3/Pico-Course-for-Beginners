from machine import Pin, ADC, PWM
import time
# set up pin 26 as an analog input, and pin 16 as PWM output
pot_pin = ADC(Pin(26)) 
pwm_pin = PWM(Pin(15))
# set the pin frequency (this is not duty cycle)
pwm_pin.freq(1000)

while True:
    # read the potentiometer value (0 to 65,535) and store it in a variable
    pot_value = pot_pin.read_u16() 
    # set the reading as a PWM duty cycle
    pwm_pin.duty_u16(pot_value)
  
    # uncomment the line below to print voltage instead of the RAW ADC value.
    #pot_value = pot_value * 3.3 / 65535
      
    print(pot_value)
    time.sleep(0.05)