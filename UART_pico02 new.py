from machine import UART, Pin # we need to import UART to use it
import time

# Initialize UART 1 on Pico A, TX pin is GP4 and RX pin is GP5
#changed to 0 and 1, UART 0

test_uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    test_uart.write('ON')  # Send 'ON' message to Pico B
    print("sent on")
    time.sleep(2)      # Wait for 2 seconds
    
    test_uart.write('OFF') # Send 'OFF' message to Pico B
    print("sent off")
    time.sleep(2)      # Wait for 2 seconds