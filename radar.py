import RPi.GPIO as GPIO
import pygame
import math
import time
import colors
import sys
import cv2
from target import *
from display import draw
from ultrasonicsensor import ultrasonicRead

# mesefe 50 cm e ayarli, degistirmek icin 
# mesafe durumunu degistirmek icin ultrasonicsensor modulunu degistir
# bu modulden mesafe durumunu degistir
# change scale in e and f in draw function in display module

print 'Radar Start'

# programi baslat
x = pygame.init()

pygame.font.init()

defaultFont = pygame.font.get_default_font()

fontRenderer = pygame.font.Font(defaultFont, 20)

radarDisplay = pygame.display.set_mode((1400, 800))
    
pygame.display.set_caption('Radar Screen')

# setup the servo and ultrasonic
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
buzzer = 17
GPIO.setup(buzzer,GPIO.OUT)

servoPin = 12
GPIO.setup(servoPin, GPIO.OUT)

servo = GPIO.PWM(servoPin, 50)
servo.start(7)

TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# targets list
targets = {}
xa = {}
xd = {}
ya = {}
yd = {}


try:
    while True:
    
        # rotate from 0 to 180
        
        for angle in range(0, 180):

            distance = ultrasonicRead(GPIO, TRIG, ECHO)
            
            # change the condition if the range is changed
            if distance != -1 and distance <= 50:
                targets[angle] = Target(angle, distance)
                xa[angle]=angle
                xd[angle]=distance
            draw(radarDisplay, targets, angle, distance, fontRenderer)

            angle = 180 - angle
            dc = 1.0 / 18.0 * angle + 2
            servo.ChangeDutyCycle(dc)

            time.sleep(0.001)
            

        # rotate from 180 to 0
        for angle in range(180, 0, -1):
            
            distance = ultrasonicRead(GPIO, TRIG, ECHO)
            
            # change the condition if the range is changed
            if distance != -1 and distance <= 50:
                targets[angle] = Target(angle, distance)
                ya[angle]=angle
                yd[angle]=distance
            
            draw(radarDisplay, targets, angle, distance, fontRenderer)

            angle = 180 - angle
            dc = 1.0 / 18.0 * angle + 2
            servo.ChangeDutyCycle(dc)

            time.sleep(0.001)
        time.sleep(2)
        if (xa[angle] == ya[angle] and (yd[angle] < (xd[angle] -2) or yd[angle] > (xd[angle] +2))):
            GPIO.output(buzzer,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(buzzer,GPIO.LOW)
            time.sleep(2)
        # detect if close is pressed to stop the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt
            
except KeyboardInterrupt:
    print 'Radar Exit'
    servo.stop()
    GPIO.cleanup()
    
except Exception as e:
    print e
    print 'Radar Exit'
    servo.stop()
    GPIO.cleanup()
    
    
pygame.quit()
sys.exit()
