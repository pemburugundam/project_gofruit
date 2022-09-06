import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

GPIO.output(servoPIN, True)
GPIO.output(servoPIN, False)
    
def turn90():
     p.start(0)
     p.ChangeDutyCycle(14) # left -90 deg position
     time.sleep(1)
     #p.ChangeDutyCycle(5) # neutral position
     #time.sleep(1)
     p.ChangeDutyCycle(10) # neutral position
     time.sleep(1)
     
     
def turn45():
     p.start(0)
     p.ChangeDutyCycle(12) # neutral position
     time.sleep(1)
     p.ChangeDutyCycle(10) # right +90 deg position
     time.sleep(1)


def set_default():
    p.start(0) # 
    p.ChangeDutyCycle(10)
    time.sleep(1)


    

