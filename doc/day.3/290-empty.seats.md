# Predmet Prázdne sedadlá

Vytvorte predmet prázdne sedadlá, ktorý bude mať:

* názov `prazdne sedadla`
* opis `Obyčajné letecké sedadlá.`
* v zozname vlastností len vlastnosť `EXAMINABLE`

```python
from items.features import EXAMINABLE
from items import Item


class EmptySeats(Item):
   name: str = 'prazdne sedadla'
   description: str = 'Obyčajné letecké sedadlá.'
   features: list[int] = [EXAMINABLE]
```
