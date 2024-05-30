import os
from PPYProject.src.modules.EFile import *
import readchar
from PPYProject.src.modules.FileHelper import *
from modules.Quest import Quest
from modules.Log import Log
from PPYProject.utils import auth
from PPYProject.utils import pullContent
from PPYProject.utils.printScripts import *
from PPYProject.src.modules.Status import *
from PPYProject.src.modules.Priority import *
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



    def getTask(self):
        log=pullContent.logsIds(self)

        return (str(self.name)+'\n'+
                str(self.project.id)+'\n'+
                self.description+'\n'+
                self.pirority+'\n'+
                self.status+'\n'+
                str(self.owner.id)+'\n'+
                log,'\n'+
                self.beginDate+'\n'+
                self.endDate)

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
                    log=Log(idElement,lines[1],lines[3],lines[4])
                    userFile=FileHelper(EFile.USERS.name,EFile.USERS.value)
                    if userFile.find(lines[2])==True:
                        log.owner=auth.make(lines[2])
                    log.task=self
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

    def listLogs(self):
        for log in self.logs:
            log.toString()

    def changeStatus(self):
        print("\nObecny status: ", self.status,"\nWybierz status: ")
        status = Status.get_status()
        if status!=None:
            self.status=str(status)
    def changePriori(self):
        print("\nObecny priorytet:", self.pirority, "\nWybierz Priorytet: ")
        priori=Priority.get_priori()
        if priori !=None:
            self.pirority = str(priori)
    def manageTask(self):
        goodChar = True
        while goodChar:
            print_modify_task()
            char_modify = readchar.readchar()
            match char_modify:
                case '1':
                    Log.addLog(self,self.owner)
                case '2':
                    cls()
                    self.listLogs()
                case '3':
                    self.changeStatus()
                    self.changePriori()
                    cls()
                case '4':
                    self.owner=pullContent.getUser()
                    break
                case '0':
                    break
                case _:
                    cls()
    def writeMe(self):
        fileName=str(self.id)+".txt"
        file=FileHelper(fileName,EFile.TASKS.value/fileName)
        file.write_to_file(self.getTask(),'w')

    @staticmethod
    def addTask(user):
        goodChar = True
        fileId = FileHelper(EFile.TASKS.name, EFile.TASKS.value)
        task = Task(int(fileId.lastId()) + 1,
                    input("Podaj nazwe zadania: "), input("Podaj opis zadania: "),
                    input("Podaj date rozpoczęcia: "), input("Podaj date zakończenia: "),
                    ' ', ' ')
        task.changeStatus()
        task.changePriori()
        task.owner=pullContent.getUser()
        task.project=pullContent.getProjectS(task)

        print("\n Dodano zadanie [{}] {} dla {} {} w projekcie {} {}:"
              .format(task.id, task.name, task.owner.imie, task.owner.nazwisko, task.project.name,
                      task.project.description))
        fileName = str(task.id) + ".txt"
        open(EFile.TASKS.value / fileName, 'x')
        file = FileHelper(fileName, EFile.TASKS.value / fileName)
        file.write_to_file(task.getTask(), 'a')
        return task
