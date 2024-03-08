# To run 'python <filename>' and enter
# python push_button_led.py

from gpiozero import Button, LED
import time

button = Button(2)
led  = LED(17)

while True:
    button.wait_for_press()
    print("Device has been activated !")
    led.toggle()
    time.sleep(0.5)
