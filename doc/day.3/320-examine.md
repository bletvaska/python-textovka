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
from .command import Command


class Examine(Command):
    name = 'preskumaj'
    description = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print('Neviem, čo chceš preskúmať.')

        # search for item
        else:
            # search for item in backpack
            for item in context.backpack:
                if item.name == self.param:
                    print(item.description)
                    break
            else:
                # search for item in current room
                for item in context.current_room.items:
                    if item.name == self.param:
                        print(item.description)
                        break
                else:
                    # not found
                    print('Taký predmet tu nikde nevidím.')

```
