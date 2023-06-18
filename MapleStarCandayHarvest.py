import time
from pynput.keyboard import Controller, Key

def press_key(key):
    keyboard = Controller()
    keyboard.press(key)
    keyboard.release(key)

while True:
    # 模擬按下 `，
    press_key('`')
    time.sleep(0.07)

    # 模擬按下方向鍵(下)
    press_key(Key.down)
    time.sleep(0.07)

    # 模擬按下 Enter
    press_key(Key.enter)
    time.sleep(0.07)

    # 模擬按下 `，
    press_key('`')
    time.sleep(0.07)
    
    # 模擬按下 `，
    press_key('`')
    time.sleep(0.07)
    
    # 模擬按下方向鍵(下)
    press_key(Key.down)
    time.sleep(0.07)
    
    # 模擬按下方向鍵(下)
    press_key(Key.down)
    time.sleep(0.07)

    # 模擬按下 Enter
    press_key(Key.enter)
    time.sleep(0.07)
    
    # 模擬按下 `，
    press_key('`')
    time.sleep(0.07)