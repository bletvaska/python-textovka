# O miestnostiach

kazda miestnost ma tieto vlastnosti:

* nazov - jedinecny nazov miestnosti, ktorym vieme miestnost odlisit od ostatnych miestnosti v hre
* opis -
* zoznam predmetov v miestnosti
* zoznam vychodov (susedia)


```python
from dataclasses import dataclass


@dataclass
class Room:
    name: str
    description: str
    items: list
    exits: list  # TODO ????
```
