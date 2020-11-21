from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

for seconds in range(12000):
    sleep(0.5)
    keyboard.press(Key.alt)
    keyboard.press('l')
    keyboard.release(Key.alt)
    keyboard.release('l')
    print(f'Done {seconds}')
