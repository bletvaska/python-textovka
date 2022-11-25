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
from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    description: str
    features: list = field(default_factory=list)
```

## Vlastnosti

```python
# if the item can be taken/dropped to/from backpack
MOVABLE = 1

# if it is possible to use the item
USABLE = 2

# if it is possible to make some action after item is examined
EXAMINABLE = 3
```
