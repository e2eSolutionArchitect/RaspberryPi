# To run 'python <filename>' and enter
# python push_button_led.py

from gpiozero import Button
button = Button(2)
button.wait_for_press()
print("Device Activated")
