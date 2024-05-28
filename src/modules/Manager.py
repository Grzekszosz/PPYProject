import readchar

from modules.Ludzie import Ludzie
from PPYProject.utils.printScripts import *
from PPYProject.utils.pullContent import *
from PPYProject.src.modules.FileHelper import *
from PPYProject.src.modules.EFile import *
class Manager(Ludzie):
    projectList=[]

    def __init__(self,id,imie,nazwisko,stanowisko):
        super().__init__(id,imie,nazwisko,stanowisko)

    def suck_Mine(self):
        file=FileHelper(EFile.PROJECTS.name,EFile.PROJECTS.value)
        projList=pull(file)
        for proj in projList:
          #  print(self.id,proj.name,proj.master.imie,proj.description)
            if proj.master.id==self.id:
                self.projectList.append(proj)

        ###TODO
        ###TODO dostaje liste obiektow projetkow
        ### swoje, wkładam do projectList
    def get_in(self):
        self.suck_Mine()
        while True:
            manager_menu()
            chose = readchar.readchar()
            match chose:
                case '0':
                    break
                case '1':
                    #Wyświetl zadania(w Jag.statusu, priorytetu, terminów, ludzi)
             #       idLoged = auth.login()
             #       if idLoged != -1:
             #           loged = auth.make(idLoged)
             #           welcome(loged)
                    pass
                case '2':
                    d=self.projectList[0]
                    for i in self.projectList:
                        print(i.toString())
                    #Wyświetl projekty()
                    pass
                case '3':

                    break
                case '4':
                    break
                case '5':
                    break
                case _:
                    cls()
           # try:
            #    if loged is None:
            #        cls()
            #        print("Nie poprawne kredki")
            #        continue
            #except NameError:
            #    print(print("Nie poprawne kredki"))
    def manageWorkers(self):
        print("Manaze Workers")
## TODO- Zarządzanie pracownikiem(dodaj, usuń, modyfikuj, przypiszDoZadania)
## TODO- Zarządzanie projektem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)
## TODO- Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)
## TODO- Wyświetl projekty(wg.statusu, priorytetu, terminów)
## TODO- Wyświetl zadania(wg.statusu, priorytetu, terminów, ludzi)