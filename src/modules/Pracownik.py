from modules.Ludzie import Ludzie



class Pracownik(Ludzie):
    def __init__(self, id, imie, nazwisko, stanowisko):
        super().__init__(id, imie, nazwisko, stanowisko)


    @staticmethod
    def addWorker():
        from utils.pullContent import lastPepoleId
        lastId=lastPepoleId()
        lastId=int(lastId)+1
        pracownik= Pracownik(lastId,input("Podaj imie: "),input("Podaj nazwisko: "),input("Podaj stanowisko: "))
        pracownik.setLogin()
        pracownik.setPassword()
