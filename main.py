import pyautogui
from time import sleep

from sms import SMS
import config


def check_screen():
    try:
        return pyautogui.locateOnScreen('gamefound.png', grayscale=True, confidence=.5)

    except Exception as e:
        print(f'check_screen error: {e}')


def main():
    sms = SMS(config.number, config.carrier, config.email, config.password)

    while True:
        game_found = check_screen()

        if game_found:
            sms.send("Your Overwatch game is starting!")
            print("Text sent")
            sleep(10)

    return


if __name__ == '__main__':
    main()
