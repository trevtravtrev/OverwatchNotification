import pyautogui
from time import sleep

from sms import SMS
import config


def check_screen():
    try:
        return pyautogui.locateOnScreen('gamefound.png', grayscale=True, confidence=.5)

    except Exception as e:
        print(f'check_screen error: {e}')


def main(continuous_mode):
    print("\n\nOverwatch Notification is now running...")
    sms = SMS(config.number, config.carrier, config.email, config.password)

    while True:
        game_found = check_screen()

        if game_found:
            print("\nOverwatch game starting detected...")
            sms.send("Your Overwatch game is starting!")
            print("Notification has been sent to your phone.")

            if not continuous_mode:
                return print("Overwatch Notification has terminated.")

            sleep(10)


if __name__ == '__main__':
    main(False)
