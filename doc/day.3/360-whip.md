# Predmet Bič

V module `whip.py` vytvorte predmet bič, o ktorom bude platiť:

* názov predmetu - `bic`
* opis predmetu - `Tvoj neoceniteľný pomocník..!`
* tento predmet sa bude dať preskúmať a bude sa dať použiť

```python
from items.features import MOVABLE, USABLE
from items import Item


class Whip(Item):
   name: str = 'bic'
   description: str = 'Tvoj neoceniteľný pomocník..!'
   features: list[int] = [MOVABLE, USABLE]
```
