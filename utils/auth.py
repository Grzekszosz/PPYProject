from PPYProject.src.modules.Manager import *
from PPYProject.src.modules.Pracownik import *
#Paczka metod Autoryzujących logowanie
def login():
    username = input("Podaj login:\n")
    password = input("Podaj hasło:\n")
    file = FileHelper('login', EFile.LOGIN.value)
    lines = file.read_file_all().split('\n')
    for line in lines:
        content = line.split(';')
        if len(content) == 3:
            if username.__eq__(content[1]) and password.__eq__(content[2]):
                return content[0]
    del file
    return -1

#Tworzy instancje zalogowanego usera
def make(id):
    file = FileHelper('users',EFile.USERS.value)
    lines= file.read_file_all().split('\n')
    for line in lines:
        content=line.split(';')
        if len(content)==4:
            if content[0] == id:
                del file
                if content[3] == 'Project Manager':
                    return Manager(content[0],content[1],content[2],content[3])
                else:
                     return Pracownik(content[0],content[1],content[2],content[3])