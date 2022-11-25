# O miestnostiach

kazda miestnost ma tieto vlastnosti:

* názov - jedinečný názov miestnosti, ktorym vieme miestnost odlisit od ostatnych miestnosti v hre
* opis - opis miestnosti
* zoznam predmetov v miestnosti
* zoznam východov (susedia)


```python
from dataclasses import dataclass


@dataclass
class Room:
    name: str
    description: str
    items: list
    exits: list  # TODO ????
```
