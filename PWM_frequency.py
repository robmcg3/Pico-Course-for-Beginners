from machine import Pin, PWM # we need to import PWM to use PWM

#updated for RP2040 Zero

# intialise pin 15 as a PWM output

pwm_pin = PWM(Pin(15))

# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
pwm_pin.freq(1000)

# this varaible is used to help calculate the required input from a duty cycle percentage
max = 65535

while True:
    # here we multiply max by the desired duty cycle (as a decimal), 0.2 is 20%, 0.7 is 70% and so on
    PWM_value = int(0.2 * max)
    # this line is the command that actually sets the duty cycle
    pwm_pin.duty_u16(PWM_value)