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

1. Vytvorte minimálnu korektnú kostru kódu pre spustenie hry spolu s privítaním a uvedením do situácie.

   ```python
   #!/usr/bin/env python3

   if __name__ == '__main__':
       print('Indiana Jones and his Great Escape')
   ```

    **Poznámka:** Pre spestrenie môžete použiť aj nasledovný banner:

    ```python
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("                       and his Great Escape                        ")
    print()
    ```


2. Vytvorte príkazový riadok, ktorého prompt bude v tvare `'>'` a skončí sa vtedy, keď hráč na vstupe zadá príkaz `koniec`.

   ```python
   #!/usr/bin/env python3

   if __name__ == '__main__':
       print('Indiana Jones and his Great Escape')

       line = None
       while line != 'koniec':
           line = input('> ')
   ```


3. Zabezpečte, aby program zvládol rozpoznať príkaz `koniec` nehľadiac na veľkosť písmen.

   ```python
   #!/usr/bin/env python3

   if __name__ == '__main__':
       print('Indiana Jones and his Great Escape')

       line = None
       while line != 'koniec':
           line = input('> ').lower()
   ```


4. Zabezpečte, aby programu pri rozpoznávaní príkazu nevadili biele znaky na začiatku a konci príkazu.

   ```python
   #!/usr/bin/env python3

   if __name__ == '__main__':
       print('Indiana Jones and his Great Escape')

       line = None
   	while line != 'koniec':
       	line = input('> ').rstrip().lstrip().lower()
   ```

   **Poznámka:** Kombinácia `.rstrip().lstrip()` sa dá nahradiť volaním jednej metódy `.strip()`.


5. Vytvorte príkaz `o hre`, pomocou ktorého sa zobrazia informácie o autorovi spolu s krátkou informáciou o hre.

    ```
    > o hre
    (c)2022 created by mirek
    Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.
    ```

   ```python
   #!/usr/bin/env python3

   if __name__ == '__main__':
       print('Indiana Jones and his Great Escape')

       line = None
   	while line != 'koniec':
       	line = input('> ').rstrip().lstrip().lower()

       	if line == 'o hre':
           	print('(c)2022 created by mirek')
           	print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')
   ```


6. Vytvorte príkaz `prikazy`, ktorý vypíše zoznam všetkých príkazov, ktoré sa dajú v hre použiť.

    ```python
    > prikazy
    V hre je možné použiť tieto príkazy:
    * koniec - ukončí rozohratú hru
    * o hre - zobrazí informácie o hre
    * prikazy - zobrazí zoznam dostupných príkazov v hre
    ```

   ```python
   #!/usr/bin/env python3

   if __name__ == '__main__':
       print('Indiana Jones and his Great Escape')

       line = None
       while line != 'koniec':
           line = input('> ').rstrip().lstrip().lower()

           if line == 'o hre':
               print('(c)2021 created by mirek')
               print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

           elif line == 'prikazy':
               print('V hre je možné použiť tieto príkazy:')
               print('* koniec - ukončí hru')
               print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
               print('* príkazy - vypíše zoznam príkazov hry')
   ```


7. Ak hráč zadá prázdny reťazec (napr. stlačí kláves `ENTER`), tak hra neurobí nič.

   ```python
   #!/usr/bin/env python3

   if __name__ == '__main__':
       print('Indiana Jones and his Great Escape')

       line = None
       while line != 'koniec':
           line = input('> ').rstrip().lstrip().lower()

           if line == '':  # len(line) == 0
               # pass
               continue

           elif line == 'o hre':
               print('(c)2022 created by mirek')
               print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

           elif line == 'prikazy':
               print('V hre je možné použiť tieto príkazy:')
               print('* koniec - ukončí hru')
               print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
               print('* príkazy - vypíše zoznam príkazov hry')
   ```

   **Poznamka:** Správanie príkazov `pass` a `continue` sa dá vyskúšať pridaním príkazu `print('...')` za príkaz `if-elif`. V prípade použitia príkazu `pass` sa po zadaní prázdneho príkazu zobrazia aj tri bodky. V prípade príkazu `continue` sa tieto bodky už nezobrazia, pretože sa začne vykonávať ďalšia iterácia cyklu `while`.


8. V prípade, že hráč zadá príkaz, ktorý neexistuje, tak hra vypíše na obrazovku text:

   ```
   Taký príkaz nepoznám.
   ```

    ```python
    #!/usr/bin/env python3

    if __name__ == '__main__':
        print('Indiana Jones and his Great Escape')

        line = None
        while line != 'koniec':
           line = input('> ').rstrip().lstrip().lower()

            if line == '':
                # pass
                continue

            elif line == 'o hre':
                print('(c)2022 created by mirek')
                print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

            elif line == 'prikazy':
                print('V hre je možné použiť tieto príkazy:')
                print('* koniec - ukončí hru')
                print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
                print('* príkazy - vypíše zoznam príkazov hry')

            else:
                print('Taký príkaz nepoznám.')
   ```


9. Ak teraz napíšete príkaz `koniec`, vypíše sa na obrazovku aj správa

    ```
    Taký príkaz nepoznám.
    ```

    a program sa skončí. Táto správa sa však vypísať nemá. Ošetrite toto správanie.

    ```python
    #!/usr/bin/env python3

    if __name__ == '__main__':
        print('Indiana Jones and his Great Escape')

        line = None
        while line != 'koniec':
           line = input('> ').rstrip().lstrip().lower()

            if line == '':
                # pass
                continue

            elif line == 'o hre':
                print('(c)2022 created by mirek')
                print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

            elif line == 'prikazy':
                print('V hre je možné použiť tieto príkazy:')
                print('* koniec - ukončí hru')
                print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
                print('* príkazy - vypíše zoznam príkazov hry')

            elif line == 'koniec':
                continue

            else:
                print('Taký príkaz nepoznám.')
    ```


10. V rámci implementácie príkazu `koniec` zabezpečte, aby sa pred samotným ukončením hra ešte opýtala, či chce hráč naozaj skončiť. A až po potvrdení sa hra aj naozaj ukončila.

    ```python
    elif line == 'koniec':
        line = input('Naozaj chceš skončiť? ([a]/n)? ').lower().ltrip().rstrip()
        if line in ('a', 'ano', 'y', 'yes', ''):
            print('Dakujem, ze si si zahral tuto fantasticku hru. Príď aj nabudúce.')
            game_state = states.QUIT
        else:
            continue
    ```
