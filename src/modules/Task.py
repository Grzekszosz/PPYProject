import os
from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *
from modules.Quest import Quest
from modules.Log import Log
from PPYProject.utils import auth
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
        self.priority = priority
        self.status = status
        self.owner = None
        self.logs = []
        self.project = None

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