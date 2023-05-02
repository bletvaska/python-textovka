# Príkaz `vezmi`

Vytvorte triedu `Take`, ktorá bude reprezentovať príkaz `vezmi`. Tento príkaz vezme predmet z miestnosti a vloží ho
do hráčovho batohu.

* názov príkazu: `vezmi`
* opis príkazu: `vezme predmet z miestnosti a vloží ho do batohu`

Príkaz musí spĺňať nasledovné podmienky:

   * Ak príkaz spustíme bez parametre (to znamená, že sme neuviedli, aký predmet chceme zobrať), program vypíše na
     obrazovku správu `Neviem, čo chceš zobrať.`:

      ```
      > vezmi
      Neviem, čo chceš zobrať.
      ```

   * Ak sa pokúsime zobrať predmet, ktorý sa v miestnosti nenachádza, vypíšte na obrazovku správu `Taký predmet tu
     nikde nevidím.`:

     ```
     > vezmi elektricka
     Taký predmet tu nikde nevidím.
     ```

   * Ak sa jedná o predmet, ktorý nemá nastavenú vlastnosť `MOVABLE`, tak vypíšte na obrazovku správu `Tento predmet
     sa nedá zobrať.`:

     ```
     > vezmi prazdne sedadla
     Tento predmet sa nedá zobrať.
     ```

   * Ak hráč úspešne vloží predmet do batohu, tak vypíšte na obrazovku správu:

     ```
     > vezmi bic
     Do batohu si vložil predmet bic.
     ```


## Riešenie

```python
from helpers import get_item_by_name
from items.features import MOVABLE
from .command import Command


class Take(Command):
    name = 'vezmi'
    description = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print('Neviem, čo chceš zobrať.')
            return

        # search for item
        item = get_item_by_name(self.param, context.current_room.items)

        # not found
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is item movable?
        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # take item
        context.current_room.items.remove(item)
        context.backpack.append(item)

        # render
        print(f'Do batohu si vložil predmet {item.name}.')
```
