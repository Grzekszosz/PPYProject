import os

from modules.Quest import Quest
from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *
from PPYProject.utils import auth
from modules.Task import Task
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

    def toString(self):
        print("Nazwa projektu: "+self.name+'\n'+"Opis projektu: "+self.description+'\n'+"Czas rozpoczęcia: "+self.beginDate+'\n'+"Czas zakonczenia: "+self.endDate+'\n'+"Wlasciciel projektu: "+self.master.imie+' '+self.master.nazwisko+'\n'+"Liczba taskow: "+str(len(self.tasks))+'\n'+"Liczba osob: "+str(len(self.pepole))+'\n')

    def initializeMaster(self,idMaster):
        file=FileHelper(EFile.USERS.name,EFile.USERS.value)
        if file.find(idMaster,'Project Manager') == True:
            self.master=auth.make(idMaster)
        else:
            print("Nie udało się zmapować kierownika projektu do projektu", self.name)
        pass
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

            #file=FileHelper(EFile.TASKS.name,EFile.TASKS.value/id/'.txt')

    def initializeWorkers(self,idsWorkers):
        file=FileHelper(EFile.USERS.name,EFile.USERS.value)
        for id in idsWorkers:
            if file.find(id)==True:
                self.pepole.append(auth.make(id))
