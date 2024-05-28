import datetime
class Log:
    owner=None
    task=None
    def __init__(self,id,date,description,workTime):
        self.id=id
        self.timestamp=date
        self.description=description
        self.workTime=workTime
