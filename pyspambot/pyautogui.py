import pyautogui, time, keyboard, random

words = ['spam','spambot','spammachine','bot','discordspammer','spammerbot','discordbot','spamdiscord']
waitLength = 5
breakLoop = False
try:
    while not breakLoop:
        if keyboard.is_pressed('q'):
            print('broke while loop')
            breakLoop = True
        for i in range(waitLength):
            if keyboard.is_pressed('q'):
                print('broke while loop')
                breakLoop = True
                break
            time.sleep(1)
        try:
            if keyboard.is_pressed('q'):
                print('broke while loop')
                breakLoop = True
                break
            else:
                for i in range(8):
                    if keyboard.is_pressed('q'):
                        print('broke while loop')
                        breakLoop = True
                        break
                    #time.sleep(0.5)
                    pyautogui.click()
                    pyautogui.typewrite(f"{random.choice(words)}{random.randint(1,100)}")
                    pyautogui.press('enter')
        finally:
            pass
                
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
