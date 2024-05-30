from enum import Enum

import readchar


class Status(Enum):
    OPEN = ('Otwarte')
    INPROGRES= ('W toku')
    CLOSED = ('Zamknięte')
    BLOCKED = ('Blokada')

    @classmethod
    def print_all_values(cls):
        # cls odnosi się do samej klasy EFile
        i=1
        for item in cls:
            print("[",i,"] ~",item.value)
            i+=1
        print("[0] ~Anuluj")
    @classmethod
    def number_of_values(cls):
        i=1
        list=[]
        list.append('0')
        for item in cls:
            list.append(str(i))
            i += 1
        return list
    @classmethod
    def change_status(cls):
        goodChar =True
        while goodChar:
            readStatus=readchar.readchar()
            if Status.number_of_values().__contains__(readStatus):
                goodChar=False
            match readStatus:
                case '0':
                    return None
                case '1':
                    return Status.OPEN.value
                case '2':
                    return Status.INPROGRES.value
                case '3':
                    return Status.CLOSED.value
                case '4':
                    return Status.BLOCKED.value
                case _:
                    pass
