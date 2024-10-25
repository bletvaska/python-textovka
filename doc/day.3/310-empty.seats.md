# Predmet Prázdne sedadlá

V module `empty_seats.py` vytvorte predmet prázdne sedadlá, o ktorom bude platiť:

* názov predmetu - `prazdne sedadla`
* opis predmetu - `Obyčajné letecké sedadlá.`
* tento predmet sa bude dať preskúmať

```python
from items.features import EXAMINABLE
from items import Item


class EmptySeats(Item):
   name: str = 'prazdne sedadla'
   description: str = 'Obyčajné letecké sedadlá.'
   features: list[int] = [EXAMINABLE]
```
