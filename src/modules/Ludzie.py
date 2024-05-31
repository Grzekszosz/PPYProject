from PPYProject.utils.printScripts import *
from modules.EFile import *
from modules.FileHelper import *


#KLasa nadrzędna
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

    #Ustawia nowe hasło
    def setPassword(self):
        while True:
            haslo=input("Podaj haslo: ")
            if haslo !='':
                break
        self.haslo=haslo

    #ustawia nowy login
    def setLogin(self):
        while True:
            login=input("Podaj login: ")
            if login !='':
                break
        self.login=login
    #Ustawia nowe nazwisko
    def setSurname(self):
        while True:
            nazwisko=input("Podaj nazwisko: ")
            if nazwisko != '':
                break
        self.nazwisko=nazwisko

    #Nadpisuje usera ze zmienionymi danymi (cały plik ze wszystkimi userami)
    def overWriteMe(self):

        listUser=FileHelper(EFile.USERS.name,EFile.USERS.value).read_lines()
        overUser=[]
        listLogins=FileHelper(EFile.LOGIN.name,EFile.LOGIN.value).read_lines()
        overLogin=[]
        for user in listUser:
            contet=user.split(';')
            if contet[0]==str(self.id):
                overUser.append(self.getMeUser()+'\n')
            else:
                overUser.append(contet[0]+ ";"+contet[1]+ ";"+contet[2]+ ";"+contet[3]+'\n')

        for login in listLogins:
            contet = login.split(';')
            if contet[0]==str(self.id):
                if self.haslo=='':
                    self.haslo=contet[2]
                if self.login=='':
                    self.login=contet[1]

                overLogin.append(self.getMeLogin()+'\n')
            else:
                overLogin.append(contet[0]+";"+contet[1]+";"+contet[2]+'\n')

        FileHelper(EFile.USERS.name,EFile.USERS.value).write_to_file(overUser, 'w')
        FileHelper(EFile.LOGIN.name, EFile.LOGIN.value).write_to_file(overLogin, 'w')

    #Zwraca string usera (dane usera)
    def getMeUser(self):
        return str(self.id)+ ";"+self.imie+ ";"+self.nazwisko+ ";"+self.stanowisko

    #Zwraca string usera (dane logowania usera)
    def getMeLogin(self):
        return str(self.id)+";"+self.login+";"+self.haslo

    #Dopisuje usera do pliku
    def writeMe(self):
        user='\n'+self.getMeUser()
        fileUser=FileHelper(EFile.USERS.name,EFile.USERS.value)
        fileUser.write_to_file(user,'a')
        logs='\n'+self.getMeLogin()
        fileLogs=FileHelper(EFile.LOGIN.name,EFile.LOGIN.value)
        fileLogs.write_to_file(logs,'a')

