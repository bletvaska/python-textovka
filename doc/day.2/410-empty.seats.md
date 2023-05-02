# Predmet Prázdne sedadlá

Vytvorte predmet prázdne sedadlá, ktorý bude mať:

* názov `prazdne sedadla`
* opis `Obyčajné letecké sedadlá.`
* v zozname vlastností len vlastnosť `EXAMINABLE`

```python
from dataclasses import dataclass, field

from adventure.items import EXAMINABLE
from adventure.items.item import Item


@dataclass
class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obyčajné letecké sedadlá.'
    features: list = field(default_factory=lambda: [EXAMINABLE])
```
