import readchar

from modules.Ludzie import Ludzie
#Metoda pracownika

class Pracownik(Ludzie):
    def __init__(self, id, imie, nazwisko, stanowisko):
        super().__init__(id, imie, nazwisko, stanowisko)

    #Dodaje nowego pracownika
    @staticmethod
    def addWorker():
        from utils.pullContent import lastPepoleId
        lastId=lastPepoleId()
        lastId=int(lastId)+1
        pracownik= Pracownik(lastId,input("Podaj imie: "),input("Podaj nazwisko: "),input("Podaj stanowisko: "))
        pracownik.setLogin()
        pracownik.setPassword()
        pracownik.writeMe()

    def get_in(self):
        print("\n\tDziękujemy za skorzystanie z wersji próbnej systemu STIPANT!\nKliknij przycisk by wyjść\n")

        readchar.readchar()
