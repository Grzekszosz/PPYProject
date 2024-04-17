import sys
import os
import readchar
#from pynput.keyboard import Listener
#from utils.keyboard import on_press
from utils.printScripts import *

def read_character():
    if os.isatty(sys.stdin.fileno()):
        import readchar
        return readchar.readchar()
    else:
        return input("Wpisz jakiś znak (i naciśnij Enter): ")

def main():
    while True:
        menu_login()
        chose = readchar.readchar()
        print(f"{chose}") 


if __name__ == '__main__':
    main()
