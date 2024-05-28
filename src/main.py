# python -m src.main
import readchar
# from pynput.keyboard import Listener
from PPYProject.utils.initializeFiles import *
from PPYProject.utils.printScripts import *
from PPYProject.utils import auth

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
                auth.login()
                #tu będe tworzyć obiekt zwrócony przez funkcje auth
                pass
            case _:
                cls()

if __name__ == '__main__':
    main()
