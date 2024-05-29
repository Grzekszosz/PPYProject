from enum import Enum
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
            print("[i] ~",item.value)
            i+=1
        print("[0] ~Anuluj")