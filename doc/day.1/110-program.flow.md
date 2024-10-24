# Program Flow

Vytvorenie hernej slučky a prvých príkazov.


## Goals

1. Porozumieť vetveniu programu pomocou príkazu `if`
2. Naučiť sa používať viacnásobné vetvenie programu pomocou príkazu `if-elif-else`
3. Porozumieť cyklom a ich ovládaniu pomocou príkazu `continue`
4. Osvojiť si základy práce s reťazcami
5. Hodnota `None`
6. Práca s jednoduchými aj zloženými logickými výrazmi
7. Prázdny príkaz `pass`


## Content

### Let's Play!

1. Miesto reťazca `Hello world!` vypíšte na obrazovku reťazec `Indiana Jones and his Great Python Adventure`.

    ```python
    print('Indiana Jones and his Great Python Adventure')
    ```

2. Pomocou funkcie `input` načítajte od hráča vstup do premennej `line`.

   ```python
   print('Indiana Jones and his Great Python Adventure')
   line = input('> ')
   ```


### Vetvenie programu

1. Vytvorte príkaz `o hre`, pomocou ktorého sa zobrazia informácie o autorovi spolu s krátkou informáciou o hre.

    ```
    > o hre
    (c)2022 created by mirek
    Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.
    ```

    ```python
    print('Indiana Jones and his Great Python Adventure')

    line = input('> ')

    if line == 'o hre':
        print('(c)2022 created by mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')
    ```

2. **Lab:** Vytvorte príkaz `prikazy`, ktorý vypíše zoznam všetkých príkazov, ktoré sa dajú v hre použiť.

    ```python
    > prikazy
    V hre je možné použiť tieto príkazy:
    * o hre - zobrazí informácie o hre
    * prikazy - zobrazí zoznam dostupných príkazov v hre
    ```

    ```python
    print('Indiana Jones and his Great Python Adventure')

    line = input('> ')

    if line == 'o hre':
        print('(c)2021 created by mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

    elif line == 'prikazy':
        print('V hre je možné použiť tieto príkazy:')
        print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
        print('* príkazy - vypíše zoznam príkazov hry')
    ```

3. V prípade, že hráč zadá príkaz, ktorý neexistuje, tak hra vypíše na obrazovku text:

    ```
    Taký príkaz nepoznám.
    ```

    ```python
    print('Indiana Jones and his Great Python Adventure')

    line = input('> ')

    if line == 'o hre':
        print('(c)2022 created by mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

    elif line == 'prikazy':
        print('V hre je možné použiť tieto príkazy:')
        print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
        print('* príkazy - vypíše zoznam príkazov hry')

    else:
        print('Taký príkaz nepoznám.')
   ```

4. Ak hráč zadá prázdny reťazec (napr. stlačí kláves `ENTER`), tak hra neurobí nič.

    ```python
    print('Indiana Jones and his Great Python Adventure')

    line = input('> ')

    if line == '':  # len(line) == 0
        pass

    elif line == 'o hre':
        print('(c)2022 created by mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

    elif line == 'prikazy':
        print('V hre je možné použiť tieto príkazy:')
        print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
        print('* príkazy - vypíše zoznam príkazov hry')

    else:
        print('Taký príkaz nepoznám.')
    ```

    **Poznamka:** Správanie príkazov `pass` a `continue` sa dá vyskúšať pridaním príkazu `print('...')` za príkaz `if-elif`. V prípade použitia príkazu `pass` sa po zadaní prázdneho príkazu zobrazia aj tri bodky.


### Cyklus

1. Zabezpečte, aby sa hra neukončila dovtedy, pokiaľ hráč nezadá príkaz `koniec`.

   úloha sa dá vyriešiť viacerými spôsobmi:

   * kontrolovať reťazec `koniec` v podmienke cyklu
   * ukončiť cyklus jeho prerušením pomocou príkazu `break`

   Začať môžeme tým, že to spravíme zle pomocou nekonečného cyklu.

   ```python
   print('Indiana Jones and his Great Python Adventure')

   while True:
        print('Indiana Jones and his Great Python Adventure')

        line = input('> ')

        if line == '':  # len(line) == 0
            pass

        elif line == 'o hre':
            print('(c)2023 created by mirek')
            print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

        elif line == 'prikazy':
            print('V hre je možné použiť tieto príkazy:')
            print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
            print('* príkazy - vypíše zoznam príkazov hry')

        elif line == 'koniec':
            break

        else:
            print('Taký príkaz nepoznám.')
   ```

2. Vyriešte úlohu tak, aby sa cyklus riadil podmienkou pre jeho ukončenie.

   ```python
   print('Indiana Jones and his Great Python Adventure')

   line = None
   while line != 'koniec':
        print('Indiana Jones and his Great Python Adventure')

        line = input('> ')

        if line == '':  # len(line) == 0
            pass

        elif line == 'o hre':
            print('(c)2022 created by mirek')
            print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

        elif line == 'prikazy':
            print('V hre je možné použiť tieto príkazy:')
            print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
            print('* príkazy - vypíše zoznam príkazov hry')

        elif line == 'koniec':
            print('Ďakujem, že si si zahral túto hru.')

        else:
            print('Taký príkaz nepoznám.')
   ```

3. **Lab:** V rámci implementácie príkazu `koniec` zabezpečte, aby sa pred samotným ukončením hra ešte opýtala, či chce hráč naozaj skončiť. A až po potvrdení sa hra aj naozaj ukončila.

    ```python
    elif line == 'koniec':
        choice = input('Naozaj chceš skončiť? (a/n)? ')
        if choice == 'a':
            print('Dakujem, ze si si zahral tuto fantasticku hru. Príď aj nabudúce.')
        else:
            line = None
    ```


### Ošetrenie vstupu

1. Zabezpečte, aby program zvládol rozpoznať príkaz `koniec` nehľadiac na veľkosť písmen.

    ```python
    print('Indiana Jones and his Great Python Adventure')

    line = None
    while line != 'koniec':
        line = input('> ').lower()
    ```

2. Zabezpečte, aby programu pri rozpoznávaní príkazu nevadili biele znaky na začiatku a konci príkazu.

    ```python
    print('Indiana Jones and his Great Python Adventure')

    line = None
    while line != 'koniec':
        line = input('> ').rstrip().lstrip().lower()
    ```

   **Poznámka:** Kombinácia `.rstrip().lstrip()` sa dá nahradiť volaním jednej metódy `.strip()`.

3. Rovnaký spôsob použite aj na ošetrenie vstupu v prípade potvrdenia ukončenia programu.
