# Rozhliadnutie sa v miestnosti

Ak chceme "vykresliť" miestnosť, musíme to urobiť pomocou samostatného vypisovania jednotlivých položiek miestnosti
ručne. V princípe sa jedná o krátky fragment kódu pre vypísanie opisu miestností, zoznamu predmetov v nej a zoznamu
východov z nej.

Miesto toho, aby sme to robili takto pracne, vytvoríme na tento účel priamo v triede `Room` metódu `.show()`, ktorá
to urobí za nás.


## Lab: Aktualizácia triedy `Room`

V triede `Room` vytvorte inštančnú metódu `.show()`. Táto metóda nebude mať žiadny parameter a po jej zavolaní sa
vypíše na obrazovku opis miestnosti, zoznam východov z miestnosti a zoznam predmetov nachádzajúcich sa v miestnosti.
Výstup môže vyzerať nasledovne:

```
Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože
motory sú vypnuté a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že áno?)

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

Ak používate modul rich na farebný výpis, tak:

* predmety vypíšte fialovou farbou (`magenta`)
* východy z miestnosti vypíšte žltou farbou (`yellow`)


## Riešenie

```python
from pydantic import BaseModel


class Room(BaseModel):
    # fields
    name: str
    description: str
    items: list = []
    exits: list = []

    def show(self):
        """
        Shows the current room.
        """
        print(self.description)
        print('Vidíš:')
        for item in self.items:
            print(item.name)
```
