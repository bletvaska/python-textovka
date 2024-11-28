# Pokročilé preskúmanie predmetu

Po preskúmaní prázdnych sedadiel spoza nich vypadne padák. Začneme teda tým, že vytvoríme padák, ktorý spoza nich
vypadne a potom zabezpečíme, aby ten padák po preskúmaní naozaj vypadol.


## Padák

V triede `Parachute` v module `parachute.py` vytvorte predmet padák. O tomto predmete platí:

* názov bude: `padak`
* opis bude: `Obyčajný padák. Made in U.S.A. 1933`
* zoznam vlastností: prenositeľný a použiteľný


## Riešenie

```python
from items.item import Item
from items.features import MOVABLE, USABLE


class Parachute(Item):
   name: str = "padak"
   description: str = "Obyčajný padák. Made in U.S.A. 1933"
   features: list[int] = [MOVABLE, USABLE]
```
