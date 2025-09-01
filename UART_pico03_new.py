from machine import UART, Pin

# Initialize UART 1 on Pico B, TX pin is GP4 and RX pin is GP5


#changed to 0 and 1, UART 0

test_uart2 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# set up onboard LED
led = Pin("LED", Pin.OUT)

while True:
    # Check if anything is available in buffer
    if test_uart2.any():
        
        # recieve and store the message in a variable
        message = test_uart2.read().decode() # this .decode() removes the byte string format
        print(message)
        
        # control the led based on the string
        if message == "ON":
            led.value(1)
            
        elif message == "OFF":
            led.value(0)