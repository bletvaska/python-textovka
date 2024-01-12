# Indyho voľný pád

Aktuálne Indiana Jones letí vo vzduchu a zem sa pomaly približuje. V batohu má padák (ak si ho nezabudol zobrať v
lietadle) a potrebuje ho otvoriť.

To však nie je všetko. Použitie padáku je jediný príkaz, ktorý je možné v tejto ošemetnej situácii urobiť. Ak tak
neurobí, zomrie.

Vytvorte preto samostatnú miestnosť `FreeFall`, ktorá bude reprezentovať miestnosť s názvom `vo vzduchu`. Zabezpečte,
aby v prípade, že Indy napíše viac príkazov ako jeden, zomrel.


## Riešenie

```python
import states
from items.empty_seats import EmptySeats
from items.whip import Whip
from . import directions
from .room import Room


class FreeFall(Room):
    name: str = 'voľný pád'
    description: str = 'Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a nevšímaj si zem, ktorá sa rapídne približuje. Mimochodom, v diaľke na [bold yellow]juhu[/bold yellow] je vidieť nejaký vojenský tábor.'

    def act(self, context):
         print('Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie ako skok hlboký.')
         context.game_state = states.STATE_DEATH
```
