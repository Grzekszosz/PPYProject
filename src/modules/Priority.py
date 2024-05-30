from enum import Enum

import readchar


class Priority(Enum):
    VERYLOW = ('Bardzo niski')
    LOW = ('Niski')
    NORMAL = ('Normalny')
    HIGH = ("Wysoki")
    VERYHIGH=("Bardzo wysoki")

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
    def get_priori(cls):
        goodChar =True
        while goodChar:
            readPriori=readchar.readchar()
            if Priority.number_of_values().__contains__(readPriori):
                goodChar=False
            match readPriori:
                case '0':
                    return None
                case '1':
                    return Priority.VERYLOW.value
                case '2':
                    return Priority.LOW.value
                case '3':
                    return Priority.NORMAL.value
                case '4':
                    return Priority.HIGH.value
                case '5':
                    return Priority.VERYHIGH.value
                case _:
                    pass