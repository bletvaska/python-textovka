# Príkaz `poloz`

Vytvorte triedu `Drop`, ktorá bude reprezentovať príkaz `poloz`. Tento príkaz položí predmet z batohu do aktuálnej
miestnosti.

* názov príkazu: `poloz`
* opis príkazu: `vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti`

Príkaz musí spĺňať nasledovné podmienky:

   * Ak príkaz spustíme bez parametre (to znamená, že sme neuviedli, aký predmet chceme položiť), program vypíše na
     obrazovku správu `Neviem čo chceš položiť.`:

      ```
      > poloz
      Neviem čo chceš položiť.
      ```

   * Ak sa pokúsime položiť predmet, ktorý pri sebe nemáme, vypíšte na obrazovku správu `Taký predmet pri sebe nemáš.`:

     ```
     > poloz elektricka
     Taký predmet pri sebe nemáš.
     ```

   * Ak hráč úspešne položí predmet do miestnosti, vypíšte na obrazovku správu:

     ```
     > poloz bic
     Do miestnosti si položil bic.
     ```


## Riešenie

```python
from rich import print

from helpers import get_item_by_name
from .command import Command


class Drop(Command):
    name: str = 'poloz'
    description: str = 'vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti'

    def exec(self, context):
        item_name = self.param

        # if no item was entered
        if item_name == '':
            print('Neviem, čo chceš položiť.')
            return

        # search for item
        item = get_item_by_name(item_name, context.backpack)

        # not found
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # take item
        context.backpack.remove(item)
        context.current_room.items.append(item)

        # render
        print(f'Do miestnosti si položil predmet [bold magenta]{item.name}[/bold magenta].')
```
