# Príkazy pre pohyb po svete

## Príkaz `dolu`

V triede `Down` vytvorte príkaz `DOLU`, pomocou ktorého sa hráč presunie do miestnosti, ktorá sa nachádza dolu od
aktuálnej.

Príkaz bude mať tieto vlastnosti:

* názov príkazu: `dolu`
* opis príkazu: `presunie sa do miestnosti dolu od aktuálnej`

Príkaz musí spĺňať nasledovné podmienky:

* V prípade, že sa daným smerom nedá ísť, vypíšte na obrazovku správu:

   ```
   Tam sa nedá ísť.
   ```

* Po úspešnom prejdení do cieľovej miestnosti na západ od aktuálnej sa v miestnosti rovno rozhliadnite.


## Riešenie

```python
from helpers import get_room_by_name
from rooms import directions
from .command import Command


class Down(Command):
    name = 'dolu'
    description = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        if directions.DOWN in context.current_room.exits:
            room = context.current_room.exits[directions.DOWN]
            context.current_room = get_room_by_name(room, context.world)
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
