# Indyho voľný pád

Aktuálne Indiana Jones letí vo vzduchu a zem sa pomaly približuje. V batohu má padák (ak si ho nezabudol zobrať v
lietadle) a potrebuje ho otvoriť.

To však nie je všetko. Použitie padáku je jediný príkaz, ktorý je možné v tejto ošemetnej situácii urobiť. Ak tak
neurobí, zomrie.

Vytvorte preto samostatnú miestnosť `FreeFall`, ktorá bude reprezentovať miestnosť s názvom `vo vzduchu`. Zabezpečte,
aby v prípade, že Indy napíše viac príkazov ako jeden, zomrel. V prípade smrti vypíšte na obrazovku červenou
farbou správu:

```
Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie ako skok hlboký.
```

Stav hry po Indyho smrti nastavte na `DEATH_BY_FREE_FALL`.


## Riešenie

```python
from rich import print

import states
from .room import Room


class FreeFall(Room):
    def act(self, context):
        print('[bold red]Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie '
              'ako skok hlboký. [/bold red]')
         context.game_state = states.DEATH_BY_FREE_FALL
```
