from gpiozero import Servo
from time import sleep

servo = Servo(17)  # Replace 17 with the actual GPIO pin number

# servo.value = 0.5  # Move to the middle position
# sleep(1)          # Hold for 1 second

# servo.value = 0   # Move back to the starting position
# sleep(1)          # Hold for 1 second

# servo.value = 0.75   # Move back to the starting position
# sleep(1)  





#move 180 degrees
servo.min()
sleep(1)
servo.max()
sleep(1)
servo.min()
sleep(1)



servo.close()     # Clean up GPIO resources