# Príkaz `preskumaj`

Vytvorte príkaz `preskumaj`, pomocou ktorého zobrazíte opis zvoleného predmetu.

* Ak predmet nebol v príkaze uvedený, vypíšte na obrazovku správu:

   ```
   > preskumaj
   Neviem, čo chceš preskúmať.
   ```

* Ak hráč napíše názov predmetu, ktorý sa v batohu nenachádza, vypíšte na obrazovku správu:

   ```
   > preskumaj elektricka
   Taký predmet pri sebe nemáš.
   ```

* Ak hráč napíše názov predmetu, ktorý sa v batohu nachádza, tak na obrazovku vypíšte jeho opis

   ```
   > preskumaj bic
   Tvoj neoceniteľný kamarát na každom jednom dobrodužstve.
   ```

```python
from dataclasses import dataclass

from adventure.helpers import get_current_room, get_item_by_name
from .command import Command


@dataclass
class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš preskúmať.")
            return

        # search for item
        room = get_current_room(context)
        item = get_item_by_name(self.param, context.backpack + room.items)

        # was found?
        if item is None:
            print("Taký predmet tu nikde nevidím.")
            return

        # render
        print(item.description)
```
