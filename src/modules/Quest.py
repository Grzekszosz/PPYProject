class Quest:
    iduniq =0
    id=''
    description=''
    beginDate=''
    endDate=''
    def __init__(self, id, description='', begin_date='', end_date=''):
        self.id = id
        self.description = description
        self.beginDate = begin_date
        self.endDate = end_date

    def suck_Mine(self):
        pass