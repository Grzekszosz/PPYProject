# Stipant

## System zarządzania projektami

### Opis:

#### Aplikacja do zarządzania projektami, która umożliwia tworzenie projektów, dodawanie zadań do projektów, przypisywanie zadań do członków zespołu i śledzenie postępu.

### Wymagania:

1. Tworzenie nowych projektów z opisem i datami rozpoczęcia i zakończenia.
2. Dodawanie zadań do projektów z szczegółami takimi jak opis, priorytet, terminy, osoba odpowiedzialna
3. Wyswietlanie listy projektów i zadań.
4. Edycja i usuwanie projektów i zadań.
5. Filtracja projektów/zadań według statusu, priorytetu, terminów.
6. Interaktywny interfejs użytkownika.
7. Zarządzanie pracownikami(imię, nazwisko, stanowisko)
8. Obsługa błędów i odpowiednie komunikaty dla użytkownika.
9. Dodawanie logow do zadan od pracownikow wraz z czasem przeznaczonym
10. Wykorzystanie plików i folderów w formie 'bazy'
### Opis Klas
robie zmiane 
**Misja**:
- id(*unikalny*)
- nazwa
- opis
- data rozpoczęcia
- data zakończenia

**Projekt** *extends: Misja*::
- podpięte zadania
- przypisane osoby
- osoba prowadząca
- liczba zaplanowanych godzin(**calculate:** *suma godzin z zadań*) **
- liczba poświęconych godzin(**calculate:** *suma godzin z logow podpiętych zadań*)***
- postęp (**calculate:** *suma zaplanowanych ukończonych godzin z zadań(ukończone) / suma godzin z zadań zaplanowanych(w toku, otwarte, blokada)*)****


**Zadania** *extends: Misja*:
- priorytet (*bardzo niski, niski, normalny, wysoki, bardzo wysoki*)
- status (*otwarte, w toku, zamknięte, blokada*)
- podpięte podzadanie (zadanie)
- przypisane osoby (*wraz z przydzielonym czasem ile powinno zająć zadanie*)
- osoba odpowiedzialna
- czas zaplanowany
- czas poswiecony
- postęp (**calculate:** *suma godzin z pod zadań / suma godzin wykonanych zadań*)
- logi_pracy

**Log**:
- id
- czas(*timestamp*)
- autor(*class:* **pracownicy**)
- opis
- czas przepalony

**Ludzie**:
- id
- imie
- nazwisko
- login
- hasło
- stanowisko
- przypisane Zadania 

**Kierownictwo** *extends: Ludzie*:
- przypisaneProjekty
####
  ***Metody:***
- Zarządzanie pracownikiem(dodaj, usuń, modyfikuj, przypiszDoZadania)
- Zarządzanie projektem(dodaj, usuń, modyfikuj, przypisz/utworzZadania)
- Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz/utworzZadania)
- Wyświetl projekty(wg. statusu, priorytetu, terminów)
- Wyświetl zadania(wg. statusu, priorytetu, terminów, ludzi)

**Pracownicy** *extends: Ludzie*:
####
***Metody:***
- Wyświetl projekty(przypisane do pracownika)
- Zarządzanie zadaniem(modyfikuj *(status, logi_pracy)* )
- Wyświetl zadania(wg. statusu, priorytetu, terminów, ludzi - przypisane do mnie)

**Files:**
- nazwa **(Enum: *Folders*)**
- sciezka
***Metody***
- Inicjalizuj projekt
- Otworz plik
- Utworz plik
- Dodaj do pliku
- Usun z pliku
- Utworz Log per Zadanie

###### ENUM: **Folders**
1. Pracownicy      
2. Projekty        
3. Zadania         
4. Log             




## Licencja

[MIT](https://choosealicense.com/licenses/mit/)

