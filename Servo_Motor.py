import time
from servo import Servo

my_servo = Servo(pin_id=0)

my_servo.write(0)
time.sleep(2.0)
my_servo.write(30)
time.sleep(2.0)
my_servo.write(60)
time.sleep(2.0)
my_servo.write(90)