import time
import board
import pwmio
from adafruit_motor import servo

# Create a PWMOut object on Pin D26.
pwm = pwmio.PWMOut(board.D26, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    # Move servo to 0 degrees
    my_servo.angle = 0
    time.sleep(1)
    # Move servo to 20 degrees
    my_servo.angle = 50
    time.sleep(1)
    # Move servo to 130 degrees
    my_servo.angle = -50
    time.sleep(1)