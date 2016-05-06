import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

count = 0

def morsecode():
    
    '''dot dot dot'''
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)

    '''dash dash dash'''
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)
    
    '''dot dot dot'''
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    
os.system('clear')
print('Morse Code')

loop_count = input('How many times would you like the SOS to loop?: ')
while loop_count > 0:
    loop_count = loop_count - 1
    morsecode()