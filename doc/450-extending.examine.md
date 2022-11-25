#

## Predmet padak

vytvorte padak

```python
from dataclasses import dataclass, field

from items.features import MOVABLE, USABLE, EXAMINABLE
from items.item import Item


@dataclass
class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE, EXAMINABLE])
```
