from enum import Enum
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
            print("[i] ~",item.value)
            i+=1
        print("[0] ~Anuluj")