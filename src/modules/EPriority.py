from enum import Enum

import readchar

#ENUM dla priorytetu
class EPriority(Enum):
    VERYLOW = ('Bardzo niski')
    LOW = ('Niski')
    NORMAL = ('Normalny')
    HIGH = ("Wysoki")
    VERYHIGH=("Bardzo wysoki")

    #Drukuje wszystkie wartości
    @classmethod
    def print_all_values(cls):
        # cls odnosi się do samej klasy EFile
        i=1
        for item in cls:
            print("[",i,"] ⚡~",item.value)
            i+=1
        print("[0] ~Anuluj")

    #Zwraca liczbe ENUMA
    @classmethod
    def number_of_values(cls):
        i=1
        list=[]
        list.append('0')
        for item in cls:
            list.append(str(i))
            i += 1
        return list

    #Zwraca wybrany priorytet
    @classmethod
    def get_priori(cls):
        cls.print_all_values()
        goodChar =True
        while goodChar:
            readPriori=readchar.readchar()
            if EPriority.number_of_values().__contains__(readPriori):
                goodChar=False
            match readPriori:
                case '0':
                    return None
                case '1':
                    return EPriority.VERYLOW.value
                case '2':
                    return EPriority.LOW.value
                case '3':
                    return EPriority.NORMAL.value
                case '4':
                    return EPriority.HIGH.value
                case '5':
                    return EPriority.VERYHIGH.value
                case _:
                    pass