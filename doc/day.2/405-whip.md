# Predmet Bič

```python
from dataclasses import dataclass, field

from adventure.items import MOVABLE, USABLE
from adventure.items.item import Item


@dataclass
class Whip(Item):
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný pomocník..!'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE])
```
