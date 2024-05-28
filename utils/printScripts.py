import os
###TODO skrypty dla projektow, logow, zadan,
###TODO teksty zagniezdzajace menu dla pracownika i menagera

def cls():
    os.system("cls" if os.name == "nt" else "clear")


def menu_login():
    print("\t\t\t\t\t***Stipant***\n"
          "Wybierz opcje:\n"
          "\t[1] ~Zaloguj\n"
          "\t[0] ~Wyjdź\n")


def login_content():
    return (
        "1;Gorlowski;1234\n",
        "2;Nowak;1243\n",
        "3;Kowalski;4321\n"
    )


def users_content():
    return (
        "1;Orłowski;Grzegorz;Project.py Manager\n",
        "2;Nowak;Daniel;Dev\n",
        "3;Kowalski;Jan;Dev\n"
    )


def welcome(lud):
    cls()
    if lud.stanowisko == 'Project.py Manager':
        print("Witamy Pana {} {} MENADŻERA: ".format(lud.imie, lud.nazwisko))
    else:
        print("Dzień dobry {} {} {} : ".format(lud.imie, lud.nazwisko, lud.stanowisko))


def manager_menu():
    print(
        "[1] ~Wyświetl zadania(w Jag.statusu, priorytetu, terminów, ludzi)\n",
        "[2] ~Wyświetl projekty(wg.statusu, priorytetu, terminów)\n",
        "[3] ~Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)\n",
        "[4] ~Zarządzanie projektem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)\n",
        "[5] ~Zarządzanie pracownikiem(dodaj, usuń, modyfikuj, przypiszDoZadania)\n",
        "[0] ~Wyloguj"
    )


def worker_menu():
    print(
        "[1] ~Wyświetl zadania(wg. statusu, priorytetu, terminów, ludzi - przypisane do mnie)\n",
        "[2] ~Zarządzanie zadaniem(modyfikuj *(status, logi_pracy)* )\n",
        "[3] ~Wyświetl projekty(przypisane do pracownika)\n",
        "[0] ~Wyloguj"
    )
