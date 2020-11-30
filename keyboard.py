from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

for seconds in range(3):
    sleep(0.1)

    keyboard.press(Key.alt)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.alt)
    print(f'Foi pressionada {seconds}x.')


def pressiona(valor):
    for i in range(valor):
        i
        keyboard.press(Key.caps_lock)
        keyboard.release(Key.caps_lock)
        sleep(0.2)
        keyboard.press(Key.num_lock)
        keyboard.release(Key.num_lock)
        sleep(0.2)
        keyboard.press(Key.scroll_lock)
        keyboard.release(Key.scroll_lock)
        sleep(0.2)


pressiona(50)
