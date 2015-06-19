import Adafruit_BBIO.GPIO as GPIO
import time

# 3:7 Somac 830ml

# Motor 1
# Beer
# P8_8  : pwm , 0 -> OFF , 1 -> ON
# P8_10 : dir , 0 -> reverse , 1 -> normal
# Motor 2
# Soju
# P8_7 : pwm , 0 -> OFF , 1 -> ON
# P8_9 : dir , 0 -> reverse , 1 -> normal 

GPIO.setup("P8_8", GPIO.OUT)
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_7", GPIO.OUT)
GPIO.setup("P8_9", GPIO.OUT)

GPIO.output("P8_8", GPIO.HIGH)
GPIO.output("P8_10", GPIO.HIGH)
GPIO.output("P8_7", GPIO.HIGH)
GPIO.output("P8_9", GPIO.HIGH)

time.sleep(30)
# OFF motor 1
GPIO.output("P8_7", GPIO.LOW)
GPIO.output("P8_9", GPIO.LOW)

time.sleep(40)
GPIO.output("P8_8", GPIO.LOW)
GPIO.output("P8_10", GPIO.LOW)

# OFf motor 2
# Total 70 seconds.
GPIO.cleanup()