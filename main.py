import time

import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the servo
servo_pin = 18

# Set the frequency for the servo (50Hz is common)
frequency = 50

# Set the duty cycle for 90 degrees (1.5ms pulse width)
duty_cycle_90 = 7.5

# Set the duty cycle for 0 degrees (0.5ms pulse width)
duty_cycle_0 = 2.5

# Configure the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object with the servo pin and frequency
pwm = GPIO.PWM(servo_pin, frequency)

# Start the PWM with the duty cycle for 0 degrees
pwm.start(duty_cycle_0)

# Rotate the servo to 90 degrees
pwm.ChangeDutyCycle(duty_cycle_90)
time.sleep(1)  # Wait for 1 second

# Rotate the servo back to 0 degrees
pwm.ChangeDutyCycle(duty_cycle_0)
time.sleep(1)  # Wait for 1 second

# Stop the PWM and clean up the GPIO
pwm.stop()
GPIO.cleanup()