import datetime
from PPYProject.src.modules.FileHelper import *

class Log:
    owner=None
    task=None
    def __init__(self,id,date,description,workTime):
        self.id=id
        self.timestamp=date
        self.description=description
        self.workTime=workTime
    def toString(self):
        print("\n["+str(self.id)+"] | Data: "+str(self.timestamp)+" | Godziny: "+self.workTime+" | Zadania: "
        ""+self.task.name+"\n" +"Opis: "+self.description+"\n"+self.owner.imie+" "+self.owner.nazwisko+"\n")

    def getLog(self):
        return (str(self.task.id)+'\n'+
                str(self.timestamp)+'\n'+
                self.owner.id+'\n'+
                self.description+'\n'+
                self.workTime)

    @staticmethod
    def addLog(Task,user):
        logfile = FileHelper(EFile.LOGS.name, EFile.LOGS.value)
        log = Log(int(logfile.lastId()) + 1, datetime.datetime.now(), input("Opis: "),
                  input("Spędzony czas: "))
        log.owner = user
        Task.logs.append(log)
        log.task = Task
        fileName = str(log.id) + ".txt"
        open(EFile.LOGS.value / fileName, 'x')
        file = FileHelper(fileName, EFile.LOGS.value / fileName)
        file.write_to_file(log.getLog())
