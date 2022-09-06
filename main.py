import RPi.GPIO as GPIO
import time
from servo import *
from ultrasonic_distance import *
#import os
#from dotenv import load_dotenv

#load_dotenv

S2 = 23
S3 = 24
signal = 26 
NUM_CYCLES = 10


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(S2,GPIO.OUT)
  GPIO.setup(S3,GPIO.OUT)
  print("\n")
  



def loop(hitung1,hitung2,hitung3):
 temp = 1
while(1):  

    GPIO.output(S2,GPIO.LOW)
    GPIO.output(S3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start 
      red  = NUM_CYCLES / duration   
    
      GPIO.output(S2,GPIO.LOW)
      GPIO.output(S3,GPIO.HIGH)
      time.sleep(0.3)
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start
      blue = NUM_CYCLES / duration
      

      GPIO.output(S2,GPIO.HIGH)
      GPIO.output(S3,GPIO.HIGH)
      time.sleep(0.3)
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start
      green = NUM_CYCLES / duration
      
        
      if green<1500 and blue<1500 and red>1500:
        print("red")
        temp=1
        turn90()
        
      elif red<3000 and  blue<1500 and green>1500:
        print("green")
        temp=1
        turn45()
        
      elif green<7000 and red<7000 and blue>12000:
        print("blue")
        temp=1
        set_default()

      #elif red>10000 and green>10000 and blue>10000 and temp==1:
        #print("place the object.....")
        #temp=1
        #set_default()

      else:
        print("white")
        temp=1
        set_default()
      
      hitung_mutlak = dist_logic1(hitung1),dist_logic2(hitung2),dist_logic3(hitung3)


    def endprogram():
        GPIO.cleanup()

    if __name__=='__main__':
      
        setup()

        try:
          
           hitung_mutlak = 0
           print(hitung_mutlak)
           loop(hitung_mutlak)



        except KeyboardInterrupt:
           endprogram()