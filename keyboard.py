from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

for seconds in range(101):
    sleep(0.1)

    keyboard.press(Key.alt)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.alt)
    print(f'Foi pressionada {seconds}x.')
