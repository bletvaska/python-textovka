# Padák

Vytvorte predmet padák. O predmete plati, ze:

* trieda, v ktorej sa bude nachádzať, sa volá `Parachute`
* názov bude: `padak`
* opis bude: `Obyčajný padák. Made in U.S.A. 1933`
* zoznam vlastností: prenositeľný a použiteľný


## Riešenie

```python
from items.item import Item
from items.features import MOVABLE, EXAMINABLE


class Parachute(Item):
   name: str = "padak"
   description: str = "Obyčajný padák. Made in U.S.A. 1933"
   features: list[int] = [MOVABLE, EXAMINABLE]
```
