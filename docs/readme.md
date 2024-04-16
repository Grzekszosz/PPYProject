# Stipant 
'z łac. 'Juczny'

## System zarządzania projektami

### Opis:

#### Aplikacja do zarządzania projektami, która umożliwia tworzenie projektów, dodawanie zadań do projektów, przypisywanie zadań do członków zespołu i śledzenie postępu.

### Wymagania:

1. Tworzenie nowych projektów z opisem i datami rozpoczęcia i zakończenia.
2. Dodawanie zadań do projektów z szczegółami takimi jak opis, priorytet, terminy, osoba odpowiedzialna, osoba przydzielona, czas pracy danej osoby.
3. Wyswietlanie listy projektów i zadań.
4. Edycja i usuwanie projektów i zadań.
5. Filtracja projektów/zadań według statusu, priorytetu, terminów.
6. Interaktywny interfejs użytkownika.
7. Zarządzanie pracownikami(imię, nazwisko, stanowisko)
8. Obsługa błędów i odpowiednie komunikaty dla użytkownika.

### Opis Klas
**Projekt**:
- id
- nazwa
- opis
- data rozpoczęcia
- data zakończenia
- lista zadań
- przypisane osoby
- osoba prowadząca
- liczba zaplanowanych godzin(**calculate:** *suma godzin z zadań*)
- liczba poświęconych godzin(**calculate:** *suma godzin z logow podpiętych zadań*)
- postęp (**calculate:** *suma zaplanowanych ukończonych godzin z zadań(ukończone) / suma godzin z zadań zaplanowanych(w toku, otwarte, blokada)*)


**Zadania**:
- id(*unikalny*)
- nazwa
- opis
- priorytet (*bardzo niski, niski, normalny, wysoki, bardzo wysoki*)
- data rozpoczęcia
- data zakończenia
- podpięte podzadanie (zadanie)
- przypisane osoby (*wraz z przydzielonym czasem ile powinno zająć zadanie*)
- osoba odpowiedzialna
- postęp (**calculate:** *suma godzin z pod zadań / suma godzin wykonanych zadań*)
- logi_pracy

**Log**:
- id
- czas(*timestamp*)
- autor(*class:* **pracownicy**)
- Opis
- czas przepalony

**Ludzie**:
- id
- imie
- nazwisko
- stanowisko
- dataZatrudnienia
- dataZakonczeniaPracy
- przypisaneZadania

**Kierownictwo** *extends: Ludzie*:
- przypisaneProjekty
  ***Metody:***
- Zarządzanie pracownikiem(dodaj, usuń, modyfikuj, przypiszDoZadania)
- Zarządzanie projektem(dodaj, usuń, modyfikuj, przypisz/utworzZadania)
- Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz/utworzZadania)
- Wyświetl projekty(wg. statusu, priorytetu, terminów)
- Wyświetl zadania(wg. statusu, priorytetu, terminów, ludzi)

**Pracownicy** *extends: Ludzie*:
***Metody:***
- Wyświetl projekty(przypisane do pracownika)
- Zarządzanie zadaniem(modyfikuj *(status, logi_pracy)* )
- Wyświetl zadania(wg. statusu, priorytetu, terminów, ludzi - przypisane do mnie)


## Licencja

[MIT](https://choosealicense.com/licenses/mit/)

