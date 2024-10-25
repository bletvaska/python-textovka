# Rozhliadnutie sa v miestnosti

## Aktualizácia triedy `Room`

V triede `Room` vytvorte inštančnú metódu `.show()`. Táto metóda nebude mať žiadny parameter a po jej zavolaní sa vypíše na obrazovku opis miestnosti, zoznam východov z miestnosti a zoznam predmetov nachádzajúcich sa v miestnosti. Výstup môže vyzerať nasledovne:

```
Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že áno?)

Vidíš:
* bič
* prázdne sedadlá

Možné východy z miestnosti:
* dolu
```

Ak sa v miestnosti nebude nachádzať žiadny predmet, tak vypíšte na obrazovku správu:

```
Nevidíš tu nič zvláštne.
```

Ak z miestnosti nevedú žiadne východy, tak vypíšte na obrazovku:

```
Z miestnosti nevedú žiadne východy.
```


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
        print('Vidíš:')
        for item in self.items:
            print(item.name)
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
