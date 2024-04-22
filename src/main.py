# python -m src.main
import sys
import readchar
# from pynput.keyboard import Listener
from utils.auth import *
from utils.printScripts import *
from utils.initializeFiles import *


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
                login()
                #tu będe tworzyć obiekt zwrócony przez funkcje auth
                pass
            case _:
                cls()

if __name__ == '__main__':
    main()
