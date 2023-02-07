# Príkaz Rozhliadni sa

Vytvorte príkaz `rozhliadni sa`. Vlastnosti tohto príkazu sú:

* názov - `rozhliadni sa `
* opis - `rozhliadne sa v aktuálnej miestnosti`

Po zadaní tohto príkazu sa znovu zobrazí opis miestnosti spolu so zoznamom predmetov, ktoré sa v nej nachádzajú.

Po vytvorení príkazu nezabudnite aktualizovať zoznam príkazov hry, ktorý je dostupný po zadaní príkazu `prikazy`.

```
> rozhliadni sa
Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že áno?)
Vidíš:
  bič
  prázdne sedadlá
```

## Pokus o riešenie



```python
class LookAround(Command):
    name = 'rozhliadni sa'
    description = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self):
        print(current_room.description)
        if current_room.items != []:  # len(current_room.items) > 0
            print('Vidíš:')
            for item in current_room.items:
                print(f'  {item}')
        else:
            print('Nevidíš tu nič zvláštne.')
```

Lenže nebude fungovať, pretože premenná `current_room` nie je v tomto kontexte definovaná.


## Aktualizácia triedy `Room`

V triede `Room` vytvorte metódu `.show()`, pomocou ktorej "vykreslíte" obsah miestnosti na obrazovku.

```python
from pydantic import BaseModel


class Room(BaseModel):
    # fields
    name: str
    description: str
    items = []  # : list
    exits = []  #: list

    def show(self):
        """
        Shows the current room.
        """
        print(self.description)
        if self.items != []:  # len(current_room.items) > 0
            print('Vidíš:')
            for item in self.items:
                print(f'  {item}')
        else:
            print('Nevidíš tu nič zvláštne.')
```


## Aktualizácia príkazu `rozhliadni sa`

```python
class LookAround(Command):
    name = 'rozhliadni sa'
    description = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, room):
        room.show()

        return states.PLAYING
```
