# Príkaz `preskumaj`

Vytvorte príkaz `preskumaj`, pomocou ktorého zobrazíte opis predmetu, ktorý sa musí nachádzať v miestnosti.

O príkaze bude platiť:

* meno príkazu - `preskumaj`
* opis príkazu - `zobrazí informácie o zvolenom predmete`

O jeho správaní bude platiť nasledovné:

* Ak predmet nebol v príkaze uvedený, vypíšte na obrazovku správu:

   ```
   > preskumaj
   Neviem, čo chceš preskúmať.
   ```

* Ak hráč napíše názov predmetu, ktorý sa v miestnosti nenachádza, vypíšte na obrazovku správu:

   ```
   > preskumaj elektricka
   Taký predmet tu nikde nevidím.
   ```

* Ak hráč napíše názov predmetu, ktorý sa v miestnosti nachádza, tak na obrazovku vypíšte jeho opis

   ```
   > preskumaj bic
   Tvoj neoceniteľný pomocník..!
   ```


## Riešenie

```python
from .command import Command

class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context, param):
        if param == '':
            print('Neviem, čo chceš preskúmať.')
            return

        for item in context.current_room.items:
            if param == item.name:
                print(item.description)
                break
        else:
            print('Taký predmet tu nikde nevidím.')
```


## Lab

Aktuálne príkaz `preskumaj` hľadá len predmety, ktoré sa nachádzajú v miestnosti. Rozšírte preto implementáciu tak, aby nepreskúmal len predmety, ktoré sa nachádzajú v miestnosti, ale aj tie, ktoré sa nachádzajú v batohu.

