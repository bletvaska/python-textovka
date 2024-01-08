# Predmet Prázdne sedadlá

Vytvorte predmet prázdne sedadlá, ktorý bude mať:

* názov `prazdne sedadla`
* opis `Obyčajné letecké sedadlá.`
* v zozname vlastností len vlastnosť `EXAMINABLE`

```python
from items.features import EXAMINABLE
from items import Item


class EmptySeats(Item):
   name = 'prazdne sedadla'
   description = 'Obyčajné letecké sedadlá.'
   features = [EXAMINABLE]
```
