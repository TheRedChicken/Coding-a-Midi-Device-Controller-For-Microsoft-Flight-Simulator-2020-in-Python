import pygame.midi
from pynput.keyboard import Key, Controller
import time
import pyvjoy

pygame.midi.init()
midiIn = pygame.midi.Input(1)

keyboard = Controller()

joystick = pyvjoy.VJoyDevice(1)

while True:
    if midiIn.poll():
        data = midiIn.read(1)
        print(data)

        eventID = data[0][0][0]
        code = data[0][0][1]
        value = data[0][0][2]

        if eventID == 153 and code == 51:
            keyboard.press(Key.f6)
            time.sleep(0.05)
            keyboard.release(Key.f6)

        if eventID == 153 and code == 50:
            keyboard.press(Key.f7)
            time.sleep(0.05)
            keyboard.release(Key.f7)

        if eventID == 176 and code == 15:
            joystick.set_axis(pyvjoy.HID_USAGE_SL0, 32768 - ((value + 1) * 256))
            
        if eventID == 176 and code == 14:
            joystick.set_axis(pyvjoy.HID_USAGE_SL1, 32768 - ((value + 1) * 256))
