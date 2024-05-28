from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *


def login():
    username = input("Podaj login:\n")
#TODO Można dodać hashowane hasełka
    password = input("Podaj hasło:\n")
    file = FileHelper('users', EFile.USERS.value)
    lines = file.read_file_all().split('\n')
    for line in lines:
        content = line.split(';')
        if len(content) == 3:
            print(content[0])
            if username.__eq__(content[1]) and password.__eq__(content[2]):
                print('zalogowano')
            else:
                print('eee')



