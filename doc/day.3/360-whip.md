# Predmet Bič

V module `whip.py` vytvorte predmet bič, o ktorom bude platiť:

* názov predmetu - `bic`
* opis predmetu - `Tvoj neoceniteľný pomocník..!`
* tento predmet sa bude dať prenášať medzi miestnosťami a bude sa dať použiť

```python
from .features import MOVABLE, USABLE
from .item import Item


class Whip(Item):
   name: str = 'bic'
   description: str = 'Tvoj neoceniteľný pomocník..!'
   features: list[int] = [MOVABLE, USABLE]
```
