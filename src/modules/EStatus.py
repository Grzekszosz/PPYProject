from enum import Enum

import readchar

#ENUM dla statusu
class EStatus(Enum):
    OPEN = ('Otwarte')
    INPROGRES= ('W toku')
    CLOSED = ('Zamknięte')
    BLOCKED = ('Blokada')

    #Drukuje wszystkie wartości
    @classmethod
    def print_all_values(cls):
        # cls odnosi się do samej klasy EFile
        i=1
        for item in cls:
            print("[",i,"] ⚡~",item.value)
            i+=1
        print("[0] ~Anuluj")
    #Zwraca ile jest ENUM'a
    @classmethod
    def number_of_values(cls):
        i=1
        list=[]
        list.append('0')
        for item in cls:
            list.append(str(i))
            i += 1
        return list

    #Zwraca wybrany ENUM
    @classmethod
    def get_status(cls):
        cls.print_all_values()
        goodChar =True
        while goodChar:
            readStatus=readchar.readchar()
            if EStatus.number_of_values().__contains__(readStatus):
                goodChar=False
            match readStatus:
                case '0':
                    return None
                case '1':
                    return EStatus.OPEN.value
                case '2':
                    return EStatus.INPROGRES.value
                case '3':
                    return EStatus.CLOSED.value
                case '4':
                    return EStatus.BLOCKED.value
                case _:
                    pass
