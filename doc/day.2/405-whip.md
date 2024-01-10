# Predmet Bič

Vytvorte predmet bič, ktorý bude mať:

* názov `bic`
* opis `Tvoj neoceniteľný pomocník..!`
* v zozname vlastností bude mať vlastnosti `MOVABLE` a `USABLE`


```python
from items.features import MOVABLE, USABLE
from items import Item


class Whip(Item):
   name: str = 'bic'
   description: str = 'Tvoj neoceniteľný pomocník..!'
   features: list[int] = [MOVABLE, USABLE]
```
