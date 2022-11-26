# Game State

Stav hry.


## Goals

1. Vytvoriť vlastný modul.
2. Použitie obsahu vlastného modulu vo vlastnom programe.
3. Vytvoriť vlastnú funkciu bez parametra.


## Content

### Game State

Opakujeme sa a porušujeme DRY princíp tým, že opätovne používame zoznam príkazov reprezentujúcich koniec hry. Miesto toho, aby sme to robili, pridáme do hry stavovú premennú, pomocou ktorej budeme vedieť, či sa hra ešte hrá alebo sa už ukončila.

Problém môžeme vyriešiť tak, že vytvoríme premennú `game_state`, ktorá bude v sebe držať napr. reťazec, pomocou ktorého budeme vedieť rozlíšiť, v akom stave hra je. To môže byť napríklad:

* `"playing"` - ak sa hra ešte hrá, alebo
* `"quit"` - ak sa má hra ukončiť

V inicializácii hry túto premennú nastavíme na počiatočnú hodnotu `"playing"`:

```python
game_state = "playing"
```

A upravíme podmienku v hernej slučke:

```python
while game_state == 'playing':
```

Následne už len upravíme kód pri ošetrovaní príkazov na ukončenie hry:

```python
# quit game
elif line == 'koniec':
    game_state = 'quit'
```

Kód síce fungovať bude, ale držať info o stavoch ako reťazce a na tieto reťazce sa potom aj pýtať, nie je veľmi dobrý prístup. Jednoducho sa vieme v kóde pomýliť a urobiť preklep. Syntakticky síce bude kód v poriadku, ale nebude fungovať, pretože hodnota reťazca bude iná, ako tá, na ktorú sa budeme pýtať.

Miesto toho si na začiatku modulu vytvoríme dve premenné, ktoré budeme používať na prácu so stavom:

```python
# main state, when game is playing
STATE_PLAYING = 'playing'

# when QUIT command was entered
STATE_QUIT = 'quit'
```

Následne už len upravíme podmienku v cykle hlavnej slučky:

```python
while game_state == STATE_PLAYING:
    pass
```

A upravíme tiež kód v ošetrení príkazu `koniec`:

```python
elif line == 'koniec':
    game_state = STATE_QUIT
```

Tým pádom máme problém vyriešený. A od tohto momentu pri práci so statovými premennými bude pomáhať aj vývojové prostredie.

Izolujeme však umiestnenie stavov od zvyšku kódu a vytvoríme samostatný modul `states.py`, kde tieto premenné vložíme.

```python
# main state, when game is playing
PLAYING = 'playing'

# when QUIT command was entered
QUIT = 'quit'
```

A adekvátne aktualizujeme aj kód:

```python
#!/usr/bin/env python3
from adventure import states

if __name__ == '__main__':
    print('Indiana Jones and his Great Escape')

    # main loop
    game_state = states.PLAYING
    while game_state == states.PLAYING:
        # normalizing string
        line = input('> ').lower().lstrip().rstrip()

        # empty input
        if line == '':
            continue

        # quit game
        elif line == 'koniec':
            game_state = states.QUIT

        # about game
        elif line == 'o hre':
            print('(c)2022 created by mirek')
            print('Ďalšie veľké dobrodružstvo Indiana Jonesa. Tentokrát zápasí s jazykom Python v tmavej miestnosti.')

        # show commands
        elif line == 'prikazy':
            print('Zoznam príkazov v hre:')
            print('* koniec - ukončí rozohratú hru')
            print('* o hre - zobrazí informácie o hre')
            print('* prikazy - zobrazí príkazy, ktoré sa dajú použiť v hre')

        # unknown commands
        else:
            print('Taký príkaz nepoznám.')

    # game credits
    print('(c)2022 by mirek mocný programátor')

```

**Poznámka:** Stav sa dá reprezentovať aj pomocou enumeračných typov.

```python
from enum import Enum

class GameState(Enum):
    PLAYING = 1
    END = 2
```


### Additional Tasks

1. Upravte kód tak, aby pripúšťal aj alternatívne názvy príkazov (ich aliasy alebo ich názvy v inom jazyku). Rozšírte vašu implementáciu o tieto aliasy:

   * o hre - about, info
   * prikazy - commands, help
   * koniec - quit, q, bye

   ```python
   #!/usr/bin/env python3

   if __name__ == '__main__':
       print('Indiana Jones and his Great Escape')

       line = None
       while line not in ('koniec', 'quit', 'q', 'bye'):
           line = input('> ').rstrip().lstrip().lower()

           if line in ('o hre', 'about', 'info', '?'):
               print('(c)2021 created by mirek')
               print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')

           elif line in ('prikazy', 'commands', 'help'):
               print('Dostupné príkazy v hre:')
               print('* koniec - ukončí hru')
               print('* o hre - vypíšu sa informácie o autorovi a hre samotnej')
               print('* príkazy - vypíše sa zoznam príkazov hry')

           elif line in ('koniec', 'quit', 'q', 'bye', ''):
               continue

           else:
               print('Taký príkaz nepoznám.')
   ```
