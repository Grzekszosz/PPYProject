from PPYProject.utils.printScripts import *
from modules.EFile import *
from modules.FileHelper import FileHelper


class Ludzie:
    id= ''
    imie= ''
    nazwisko= ''
    stanowisko = ''
    login=''
    haslo=''
    def __init__(self,id,imie,nazwisko,stanowisko):
        self.id = id
        self.imie=imie
        self.nazwisko=nazwisko
        self.stanowisko=stanowisko

    def get_in(self):
        pass

    def setPassword(self):
        while True:
            haslo=input("Podaj haslo")
            if haslo !='':
                break
        self.haslo=haslo
    def setLogin(self):
        while True:
            login=input("Podaj login")
            if login !='':
                break
        self.login=login
    def writeMe(self):
        str=self.id+";"+self.imie+";"+self.nazwisko+";"+self.stanowisko
        file=FileHelper(EFile.USERS.name,EFile.USERS.value)
        file.write_to_file(str,'a')
