# python -m src.main
import sys
import readchar
# from pynput.keyboard import Listener
# from utils.keyboar1d import on_press
from utils.printScripts import *
from modules.FileHelper import *


def main():
    initialize_files()

    while True:
        menu_login()
        chose = readchar.readchar()
        print(f"{chose}")
        match chose:
            case '0':
                break
            case '1':
                pass
            case _:
                cls()

if __name__ == '__main__':
    main()
