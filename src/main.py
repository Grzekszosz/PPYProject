# python -m src.main
import readchar
# from pynput.keyboard import Listener
from PPYProject.utils.initializeFiles import *
from PPYProject.utils.printScripts import *
from PPYProject.utils import auth

def main():
    initialize_files()
    loged = None
    while True:
        menu_login()
        chose = readchar.readchar()
        print(f"{chose}")
        match chose:
            case '0':
                break
            case '1':
                idLoged=auth.login()
                if idLoged != -1:
                    loged=auth.make(idLoged)
                    welcome(loged)
                else:
                    loged=None
            case _:
                cls()
        try:
            if loged is None:
                cls()
                print("Nie poprawne kredki")
                continue
        except NameError:
            print(print("Nie poprawne kredki"))
        print("dupa")
        loged.get_in()


if __name__ == '__main__':
    main()
