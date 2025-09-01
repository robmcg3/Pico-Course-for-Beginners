import ssd1306
import time
from machine import Pin, I2C
from PiicoDev_BME280 import PiicoDev_BME280


# Initialize I2C perhipheral
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

# Initialise OLED display
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

# Initialise Atmospheric Sensor
sensor = PiicoDev_BME280() # initialise the sensor

while True:
    tempC, presPa, humRH = sensor.values() # read all data from the sensor
    
    # Clear OLED display (this wont take effect till we .show())
    oled.fill(0)

    # Display our text and variables, the right 2 numbers are the x and y coordinates of the text
    oled.text("Temp:", 5, 10)
    oled.text(str(tempC), 60, 10)
    oled.text("Press:", 5, 30)
    oled.text(str(presPa), 60, 30)
    oled.text("Humid:", 5, 50)
    oled.text(str(humRH), 60, 50)
    
    # Push changes to the display
    oled.show()