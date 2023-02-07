# O miestnostiach

kazda miestnost ma tieto vlastnosti:

* názov - jedinečný názov miestnosti, ktorym vieme miestnost odlisit od ostatnych miestnosti v hre
* opis - opis miestnosti
* zoznam predmetov v miestnosti
* zoznam východov (susedia)


```python
from pydantic import BaseModel


class Room(BaseModel):
    name: str
    description: str
    items = []  # : list
    exits = []  #: list
```

## Miestnosť v lietadle

```python
from rooms import Room


room = Room(name='v lietadle',
            description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je '
                        'tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej '
                        'duše. (Celkom zaujímavá situácia, že áno?)',
            items=['bič', 'prázdne sedadlá'],
            exits=[])
```
