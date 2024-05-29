import datetime
class Log:
    owner=None
    task=None
    def __init__(self,id,date,description,workTime):
        self.id=id
        self.timestamp=date
        self.description=description
        self.workTime=workTime
    def toString(self):
        print("["+self.id+"] | Data: "+self.timestamp+" | Godziny: "+self.workTime+" | Zadania: "
        ""+self.task.name+"\n"+"Opis: "+self.description+"\n"+self.owner.imie+" "+self.owner.nazwisko+"\n")