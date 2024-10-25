# Trieda `Item` na reprezentáciu predmetov

## Item

kazdy predmet ma tieto vlastnosti:

* nazov - nazov predmetu
* opis - opis predmetu
* vlastnosti - zoznam vlastnosti, na zaklade ktorych budem vediet, co s predmetom mozem alebo nemozem spravit

v zavislosti od toho, co bude mozne s predmetom robit, budu mat niektore predmety aj specialne metody:

+ pouzitie predmetu()
+ preskumanie predmetu()

```python
from pydantic import BaseModel


class Item(BaseModel):
   name: str
   description: str
   features: list[int] = []
```

## Vlastnosti

Zoznam prípustných vlastností uložíme do samostatného modulu `features.py`, ktorý sa bude nachádzať v balíku `items`.
Vlastnosti tentokrát môžeme reprezentovať celými číslami.

Zoznam vlastností bude vyzerať nasledovne:

```python
# if the item can be taken/dropped to/from backpack
MOVABLE = 1

# if it is possible to use the item
USABLE = 2

# if it is possible to make some action after item is examined
EXAMINABLE = 3
```
