# https://www.youtube.com/watch?v=ruVt46M71Kc

import RPi.GPIO as GPIO
import time

BUTTON_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

previous_button_state = GPIO.INPUT(BUTTON_PIN)

try:
  while True:
    time.sleep(0.01)
    button_state = GPIO.input(BUTTON_PIN)
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
      print("Button is pressed")
    else:
      print("Button is NOT pressed")  
    
    if button_state ! = previous_button_state:
      previous_button_state = button_state
      if button_state == GPIO.HIGH:
        print("Button has been released")  
        
except KeyboardInterrupt:
  GPIO.cleanup()
      

for i in range(50):
  GPIO.output(7,True)
  time.sleep(1)
  GPIO.output(7,False)
  time.sleep(1)

GPIO.cleanup()
