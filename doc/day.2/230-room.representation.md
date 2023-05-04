# O miestnostiach

kazda miestnost ma tieto vlastnosti:

* názov - jedinečný názov miestnosti, ktorým vieme miestnosť odlíšiť od ostatných miestností v hre
* opis - opis miestnosti
* zoznam predmetov v miestnosti
* zoznam východov (susedia)


## Modul `room.py` a trieda `Room`

Pre reprezentáciu miestností budeme používať samostatný modul s názvom `room.py`. Do tohto modulu umiestnime aj
implementáciu dátovej triedy pre reprezentáciu miestnosti.

```python
from pydantic import BaseModel


class Room(BaseModel):
    name: str
    description: str
    items = []  # : list
    exits = []  #: list
```
