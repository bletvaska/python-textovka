# O miestnostiach

kazda miestnost ma tieto vlastnosti:

* názov - jedinečný názov miestnosti, ktorým vieme miestnosť odlíšiť od ostatných miestností v hre
* opis - opis miestnosti
* zoznam predmetov v miestnosti
* zoznam východov (susedia)


## Modul `room.py` a trieda `Room`

Pre reprezentáciu miestností vytvoríme samostatný balík s názvom `rooms`. Do neho budeme ukladať všetky miestnosti, ako aj samotnú triedu `Room`, ktorá bude rodičom pre každú miestnosť. Túto triedu vytvoríme v module `room.py`.


## Lab

Vytvorte balík, ktorý sa bude volať `rooms`. A v tomto balíku vytvorte modul s názvom `room.py`. V tomto module vytvorte triedu `Room`, ktorá bude reprezentovať miestnosť hry. Pričom o tejto miestnosti vieme, že:

* miestnosť má meno (členská premenná `name` typu reťazec)
* miestnosť má opis (členská premenná `description` typu reťazec)
* v miestnosti sa môžu nachádzať predmety (členská premenná `items` typu zoznam reťazcov)
* z miestnosti môžu viesť rozličné východy (členská premenná `exits` typu zoznam reťazcov)

Musí platiť, že trieda `Room` je potomkom triedy BaseModel z balíka `pydantic`.


```python
from pydantic import BaseModel


class Room(BaseModel):
    name: str
    description: str
    items: list = []
    exits: list = []
```
