import os

import readchar

from modules.Quest import Quest
from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *
from PPYProject.utils import auth
from modules.Task import Task
from utils import pullContent
from utils.printScripts import *
from utils.pullContent import getUsers

#Klasa projektu

class Project(Quest):
    pepole=[]
    master=None
    tasks=[]
    def __init__(self,name,id,description,beginDate,endDate):
        super().__init__(id, description, beginDate, endDate)
        self.name = name
        self.pepole = []
        self.master = None
        self.tasks = []

    #Drukuje informacje o projekcie
    def toString(self):
        print("[",self.id,"] Nazwa projektu: "+self.name+'\n'+"Opis projektu: "
              +self.description+'\n'+"Czas rozpoczęcia: "+self.beginDate+
              '\n'+"Czas zakonczenia: "+self.endDate+'\n'+"Wlasciciel projektu: "
              +self.master.imie+' '+self.master.nazwisko+'\n'+"Liczba taskow: "
              +str(len(self.tasks))+'\n'+"Liczba osob: "+str(len(self.pepole))+'\n')

    #Ustawia osobe odpowiedzialną projektu
    def initializeMaster(self,idMaster):
        file=FileHelper(EFile.USERS.name,EFile.USERS.value)
        if file.find(idMaster,'Project Manager') == True:
            self.master=auth.make(idMaster)
        else:
            print("Nie udało się zmapować kierownika projektu do projektu", self.name)


    #Ustawia liste taskow dla projektu
    def initializeTasks(self,idsTasks):
        list=os.listdir(EFile.TASKS.value)
        for element in list:
            for id in idsTasks:
                idelement=str(element).removesuffix('.txt')
                if idelement==id:
                    file=FileHelper(id,EFile.TASKS.value/element)
                    lines=file.read_lines()
                    task=Task(id,lines[0],lines[2],lines[7],lines[8],lines[3],lines[4])
                    userFile=FileHelper(EFile.USERS.name,EFile.USERS.value)
                    if userFile.find(lines[5])==True:
                        task.owner=auth.make(lines[5])
                    task.project=self
                    task.initializeLogs(lines[6])
                    self.tasks.append(task)


    #Ustawia liste przypisanych pracownikow do projektu
    def initializeWorkers(self,idsWorkers):
        file=FileHelper(EFile.USERS.name,EFile.USERS.value)
        for id in idsWorkers:
            if file.find(id)==True:
                self.pepole.append(auth.make(id))
    #Zapisuje projekt
    def writeMe(self):
        fileName=str(self.name)+'.txt'
        file=FileHelper(fileName,EFile.PROJECTS.value/fileName)
        file.write_to_file(self.getProjectExisted(),'w')
    #Zwraca string projektu
    def getProjectExisted(self):
        taskIds=self.tasksIds()
        pepoleIds=self.pepoleIds()
        return (str(self.id)+'\n'+
                self.description+'\n'+
                self.beginDate+'\n'+
                self.endDate+'\n'+
                pepoleIds+'\n'+
                taskIds+'\n'+
                str(self.master.id))

    #Zwraca string zawierający ID podpiętych tasków
    def tasksIds(self):
        ids=''
        for taskId in self.tasks:
            ids += str(taskId.id) + ','
        ids=ids.rstrip(',')
        return ids
    #Zwraca string zawierający ID podpiętych pracowników
    def pepoleIds(self):
        ids=''
        for pepole in self.pepole:
            ids += str(pepole.id)+','
        ids=ids.rstrip(',')
        return ids
    #Zmiana odpowiedzialnego Projektu
    def changeMaster(self):
        users=getUsers()
        masters=[]
        goodChar=True
        for user in users:
            if user.stanowisko=='Project Manager':
                masters.append(user)
        if len(masters)==0:
            print("Brak kierowników w systemie!")
        while goodChar:
            for master in masters:
                print("[",master.id,"]",master.imie,' ',master.nazwisko,'\n')
            print("Wybierz nowego kierownika ⚡~id")
            char=readchar.readchar()
            for master in masters:
                if char==str(master.id):
                    self.master=master
                    print("Przypisano do projektu nowego menagera\n")
                    goodChar=False
                else:
                    cls()
    #Dodaje pracownika do Projektu
    def addWorker(self):
        goodChar = True
        potentialUser = []
        users=pullContent.getUsers()
        userIds=[]
        wrongID=[]
        for user in users:
            userIds.append(user.id)
        for id in userIds:
            for userP in self.pepole:
                if str(id) == str(userP.id):
                    wrongID.append(userP.id)

        for potential in users:
            for pId in userIds:
                if potential.id==pId and potential.id not in wrongID:
                    potentialUser.append(potential)
        while goodChar:
            pullContent.printUsers(potentialUser)
            print("Wybierz usera, którego chcesz przypisać ~id:\n"
                  "[0] ~Anuluj\n")
            char=input()
            if userIds.__contains__(char):
                for potUser in potentialUser:
                    if str(potUser.id)== char:
                        self.pepole.append(potUser)
                    goodChar=False
            if char=='0':
                goodChar = False
            else:
                cls()
    #Usuwa pracownika z projektu
    def deleteWorker(self):
        goodChar=True
        ids=[]
        for worker in self.pepole:
            ids.append(worker.id)
        while goodChar:
            pullContent.printUsers(self.pepole)
            char=input("\n[0] ~Anuluj\nWybierz którego użytkownika chcesz usunąć z projektu ~id:\n")
            if char=='0':
                goodChar=False
            elif ids.__contains__(char):
                deleteWorker=None
                for worker in self.pepole:
                    if worker.id == char:
                        deleteWorker= worker
                self.pepole.remove(deleteWorker)
                goodChar=False

    #Metoda Menu zarządzania projektem
    def manageProject(self):
        goodChar=True
        while goodChar:
            printManagmentProject()
            char=readchar.readchar()
            match char:
                case '0':
                    goodChar = False
                case '1':#Zmien odpowiedzialnego
                    self.changeMaster()
                    break
                    goodChar= False
                case '2':#Zmiana Dat projektu
                    self.beginDate=input("Podaj nową datę rozpoczęcia: ")
                    self.endDate=input("Podaj nową date zakończenia: ")
                    goodChar = False
                    pass
                case '3':#Dopisz pracownika
                    self.addWorker()
                    break
                case '4':#Usun pracownuika
                    self.deleteWorker()
                    break
                case '5':#Listuj zadania
                    for task in self.tasks:
                        task.toString()
                    pass
                case '6':#Listuj pracownikow
                    pullContent.printUsers(self.pepole)

                case _:
                    pass
        pass

    #Dodaje nowy projekt
    @staticmethod
    def addProject():
        lastId=pullContent.lastProjectId()
        lastId=int(lastId)+1
        project = Project(input("Podaj nazwe projektu: "), str(lastId),input("Podaj opis projektu: "), input("Podaj date startu: "), input("Podaj date zakonczenia: "))
        project.changeMaster()
        return project
