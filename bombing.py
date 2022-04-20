from pynput.keyboard import Key, Controller
import time 
keyboard = Controller()


with keyboard.pressed(Key.cmd):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
time.sleep(3)
keyboard.type("Terminal")
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)

keyboard.type("cd")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.type("cd Tbomb")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.type("python3 bombing.py")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

#keyboard.type("cd")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

with keyboard.pressed(Key.cmd):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
ans= int(input("Which attack would you prefer, sir? \n 1. SMS \n 2.CALL \n 3.MAIL \n Type here :  "))

if ans == 1:
    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(1)
    keyboard.type("1")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    time.sleep(7)

    keyboard.type("1")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(7)

    keyboard.type("91")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        
    target = int(input("The number of the target :  "))
    tar=str(target)
    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(1)
    keyboard.type(tar)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    quan= int(input("Quantity of sms bombs (till 5000):  "))
    qua= str(quan)
    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(1)
    keyboard.type(qua)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.type("1")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(1)
    
    keyboard.type("10")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(3)

    #keyboard.type("1")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
'''
keyboard.type("cd")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.type("cd")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
'''
