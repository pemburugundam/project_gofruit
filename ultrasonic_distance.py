#Libraries
from itertools import count
import RPi.GPIO as GPIO
from modulefinder import packagePathMap
import time
from ubi_demo import *
#import os
#from dotenv import load_dotenv

#load_dotenv

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER1 = 6
GPIO_ECHO1 = 5
GPIO_TRIGGER2 = 25
GPIO_ECHO2 = 4
GPIO_TRIGGER3 = 16
GPIO_ECHO3 = 27
  
# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)

def distance1():
#    set Trigger to HIGH
     GPIO.output(GPIO_TRIGGER1, True)

    # set Trigger after 0.01ms to LOW
     time.sleep(0.00001)
     GPIO.output(GPIO_TRIGGER1, False)

     StartTime = time.time()
     StopTime = time.time()

     # save StartTime
     while GPIO.input(GPIO_ECHO1) == 0:
         StartTime = time.time()

#     # save time of arrival
     while GPIO.input(GPIO_ECHO1) == 1:
         StopTime = time.time()

#     # time difference between start and arrival
     TimeElapsed = StopTime - StartTime
     # multiply with the sonic speed (34300 cm/s)
     # and divide by 2, because there and back
     distance1 = (TimeElapsed * 34300) / 2

     return distance1


def object_detection1(distance1, hitung1 ):
    #jika jarak dibawah 100 cm maka status adalah bahaya
    if distance1 <= 5:
        hitung1 = hitung1 + 1
        return hitung1
    else:
        hitung1 = hitung1
        return hitung1

def dist_logic1(hitung1):
    dist1 = round(distance1())
    keranjang1 = object_detection1(dist1,hitung)
    print(keranjang1)
    send_data(keranjang1)
    # print ("Measured Distance = %.1f cm" % dist)
    #print(dist)
            

    if keranjang1 == 5:
        hitung = 0
    else:
        hitung = keranjang1

        time.sleep(0.01)
    return hitung1
    
# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

def distance2():
#    set Trigger to HIGH
     GPIO.output(GPIO_TRIGGER2, True)

    # set Trigger after 0.01ms to LOW
     time.sleep(0.00001)
     GPIO.output(GPIO_TRIGGER2, False)

     StartTime = time.time()
     StopTime = time.time()

     # save StartTime
     while GPIO.input(GPIO_ECHO2) == 0:
         StartTime = time.time()

#     # save time of arrival
     while GPIO.input(GPIO_ECHO2) == 1:
         StopTime = time.time()

#     # time difference between start and arrival
     TimeElapsed = StopTime - StartTime
     # multiply with the sonic speed (34300 cm/s)
     # and divide by 2, because there and back
     distance2 = (TimeElapsed * 34300) / 2

     return distance2


def object_detection2(distance2, hitung2 ):
    #jika jarak dibawah 100 cm maka status adalah bahaya
    if distance2 <= 5:
        hitung2 = hitung2 + 1
        return hitung2
    else:
        hitung2 = hitung2
        return hitung2

def dist_logic2(hitung2):
    dist2 = round(distance2())
    keranjang2 = object_detection2(dist2,hitung2)
    print(keranjang2)
    send_data(keranjang2)
    # print ("Measured Distance = %.1f cm" % dist)
    #print(dist)
            

    if keranjang2 == 5:
        hitung2 = 0
    else:
        hitung2 = keranjang2

        time.sleep(0.01)
    return hitung2

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)

def distance3():
#    set Trigger to HIGH
     GPIO.output(GPIO_TRIGGER3, True)

    # set Trigger after 0.01ms to LOW
     time.sleep(0.00001)
     GPIO.output(GPIO_TRIGGER3, False)

     StartTime = time.time()
     StopTime = time.time()

     # save StartTime
     while GPIO.input(GPIO_ECHO3) == 0:
         StartTime = time.time()

#     # save time of arrival
     while GPIO.input(GPIO_ECHO3) == 1:
         StopTime = time.time()

#     # time difference between start and arrival
     TimeElapsed = StopTime - StartTime
     # multiply with the sonic speed (34300 cm/s)
     # and divide by 2, because there and back
     distance3 = (TimeElapsed * 34300) / 2

     return distance3


def object_detection3(distance3, hitung3 ):
    #jika jarak dibawah 100 cm maka status adalah bahaya
    if distance3 <= 5:
        hitung3 = hitung3 + 1
        return hitung3
    else:
        hitung3 = hitung3
        return hitung3

def dist_logic3(hitung3):
    dist3 = round(distance3())
    keranjang3 = object_detection3(dist3,hitung3)
    print(keranjang3)
    send_data(keranjang3)
    # print ("Measured Distance = %.1f cm" % dist)
    #print(dist)
            

    if keranjang3 == 5:
        hitung3 = 0
    else:
        hitung3 = keranjang3

        time.sleep(0.01)
    return hitung3
