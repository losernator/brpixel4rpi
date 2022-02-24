# Copyright 2022 raspigamer
# License-Identifier: MIT
# install:
# sudo python3 -m pip install --force-reinstall adafruit-blinka
# sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
# 
# run:
# sudo python3 /home/pi/brpixel4rpi/brpixel4pi.py &
import time
import os
import board
import digitalio
import neopixel
try:
    from rainbowio import colorwheel
except ImportError:
    try:
        from _pixelbuf import colorwheel
    except ImportError:
        from adafruit_pypixelbuf import colorwheel
from configs import config

# 버튼 핀 설정, LED순서
# mk_arcade_joystick_rpi기준 A:D25,B:D24,X:D15,Y:D18,TL:D14,TR:D23,start:D10,select:D9

button_pins = []
button_leds = []
button_keys = ['A', 'B', 'TR', 'X', 'Y', 'TL', 'SELECT', 'START']
for i, button in enumerate(button_keys):
    if config.get(button):
        button_pins.append(config.get(button))
        button_leds.append(config.get(button+'_led', -1))
buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

dpad_pins = []
dpad_leds = []
dpad_keys = ['UP', 'DOWN', 'LEFT', 'RIGHT']
for i, dpad in enumerate(dpad_keys):
    if config.get(dpad):
        dpad_pins.append(config.get(dpad))
        dpad_leds.append(config.get(dpad+'_led', -1))
dpads = [digitalio.DigitalInOut(pin) for pin in dpad_pins]
for dpad in dpads:
    dpad.direction = digitalio.Direction.INPUT
    dpad.pull = digitalio.Pull.UP

#NeoPixel
if config.get('neopixel_pin'):
    default_color = config.get('default_color')
    led_color = config.get('led_color')
    num_pixels = max([max(button_leds),max(dpad_leds)])+1
    if len(led_color) < num_pixels:
        for i in range (num_pixels - len(led_color)):
            led_color.append(default_color)
    pixels = neopixel.NeoPixel(config.get('neopixel_pin'), num_pixels, auto_write=False)
    pixels.brightness = config.get('led_brightness')
    fadingstep = config.get('fadingstep')
    activetime = config.get('activetime')
    Neopixel = True
else :
    Neopixel = False

#레인보우 효과
def rainbow(speed):
    ebreak = False
    while True:
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j*10
                pixels[i] = colorwheel(pixel_index & 255)
            for i, button in enumerate(buttons):
                if not button.value:
                    ebreak = True
                    break
            for i, hat in enumerate(dpads):
                if not hat.value:
                    ebreak = True
                    break
            if (ebreak):
                break
            pixels.show()
            time.sleep(speed)
        if (ebreak):
            break

#컬러 변경
def colorchase(color, speed):
    ebreak = False
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(speed)
        pixels.show()
        for i, button in enumerate(buttons):
            if not button.value:
                ebreak = True
                break
        for i, hat in enumerate(dpads):
            if not hat.value:
                ebreak = True
                break
        if (ebreak):
            break
    time.sleep(0.5)

def pixelfading(index):
    if pixels[index][0]+pixels[index][1]+pixels[index][2] > 0:
        pixels[index]=(max([pixels[index][0] - pixels[index][0]/255 * fadingstep,0]), max([pixels[index][1] - pixels[index][1]/255 * fadingstep,0]), max([pixels[index][2] - pixels[index][2]/255 * fadingstep,0]))

current_time = time.monotonic()

while True:
    if Neopixel:
        if time.monotonic() - current_time > activetime:
            rainbow(0.05)
    # Button pressed value = False
    for i, button in enumerate(buttons):
        if not button.value:
            if not button_leds[i] == -1 and Neopixel:
                pixels[button_leds[i]] = led_color[button_leds[i]]
            current_time = time.monotonic()
        else:
            if not button_leds[i] == -1 and Neopixel:
                pixelfading(button_leds[i])
    # Direction
    for i, dpad in enumerate(dpads):
        if not dpad.value:
            if not dpad_leds[i] == -1 and Neopixel:
                pixels[dpad_leds[i]] = led_color[dpad_leds[i]]
            current_time = time.monotonic()
        else:
            if not dpad_leds[i] == -1 and Neopixel:
                pixelfading(dpad_leds[i])
    if Neopixel:
        pixels.show()
    time.sleep(0.03)
