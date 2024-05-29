import os
from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *
from modules.Quest import Quest
from modules.Log import Log
from PPYProject.utils import auth
from PPYProject.utils import pullContent
# priorytet(*bardzoniski, niski, normalny, wysoki, bardzowysoki *)
#(*otwarte, wtoku, zamknięte, blokada *)
class Task(Quest):
    pirority=''
    status=''
    owner=None
    logs=[]
    project=None
    name=''
    def __init__(self, id, name, description, begin_date, end_date, priority, status):
        super().__init__(id, description, begin_date, end_date)
        self.name = name
        self.pirority = priority
        self.status = status
        self.owner = None
        self.logs = []
        self.project = None

    def toString(self):
        print("\n\n"+
               "Id: "+self.id+'\n'+
              "Nazwa zadania: "+self.name+'\n'+
               "Opis: "+self.description+'\n'+
              "Prirorytet: "+self.pirority+'\n'+
              "Status: "+self.status+'\n'+
              "Wlasciciel: "+self.owner.imie+' '+self.owner.nazwisko+'\n'+
              "Projekt: "+self.project.name+'\n')

    def initializeLogs(self,idsLogs):
        list=os.listdir(EFile.LOGS.value)
        for element in list:
            for id in idsLogs:
                idElement=str(element).removesuffix('.txt')
                if idElement == id:
                    file=FileHelper(id,EFile.LOGS.value/element)
                    lines=file.read_lines()
                    log=Log(lines[0],lines[1],lines[3],lines[4])
                    userFile=FileHelper(EFile.USERS.name,EFile.USERS.value)
                    if userFile.find(lines[2])==True:
                        log.owner=auth.make(lines[2])
                    log.Task=self
                    self.logs.append(log)

    def initializeOwner(self, idOwner):
        file = FileHelper(EFile.USERS.name, EFile.USERS.value)
        if file.find(idOwner,'owner') == True:
            self.owner = auth.make(idOwner)

    def initalizeProj(self,idTask):
        listProj=os.listdir(EFile.PROJECTS.value)
        for Proj in listProj:
            file = FileHelper(Proj,EFile.PROJECTS.value/Proj)
            if file.find(idTask):
                self.project=pullContent.getProject(idTask)
                print("Znaleziono Projekt Taska",self.project.name)