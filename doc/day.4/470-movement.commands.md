# Príkazy pre pohyb po svete

## Príkaz `dolu`

V triede `Down` vytvorte príkaz `DOLU`, pomocou ktorého sa hráč presunie do miestnosti, ktorá sa nachádza dolu od
aktuálnej. V prípade, že sa daným smerom nedá ísť, vypíšte na obrazovku správu:

```
Tam sa nedá ísť.
```

Po úspešnom prejdení do cieľovej miestnosti na západ od aktuálnej sa v miestnosti rovno rozhliadnite (vypíšte jej opis).

```python
from helpers import get_room_by_name
from rooms.directions import DOWN
from .command import Command


class Down(Command):
    name = 'dolu'
    description = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        if DOWN in context.current_room.exits:
            context.current_room = get_room_by_name(context.current_room.exits[DOWN], context.world)
            context.current_room.show()
        else:
            print('Tam sa nedá ísť.')
```


## Ostatné príkazy

Podobným spôsobom implementujte aj ostatné príkazy pre pohyb. Konkrétne:

* `sever`
* `juh`
* `vychod`
* `zapad`
* `hore`
