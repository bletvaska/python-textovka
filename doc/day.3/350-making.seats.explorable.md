# Preskumatelne sedadla

Po preskúmaní sedadiel spoza nich vypadne predmet padák. Začneme teda tým, že si tento predmet vytvoríme.

## Predmet `padak`

```python
from .features import MOVABLE
from .item import Item


class Parachute(Item):
    name = 'padak'
    description = 'Obyčajný padák MADE IN U.S.A. 1933'
    features = [MOVABLE]
```

## Preskumatelne sedadla

```python
from context import Context
from .features import EXPLORABLE
from .item import Item
from .parachute import Parachute


class EmptySeats(Item):
    name = 'prazdne sedadla'
    description = 'Obvyklé letecké sedadlá.'
    features = [EXPLORABLE]

    def explore(self, context: Context):
        context.current_room.items.append(Parachute())
        print('Pod jedným z nich si našiel padák. Šťastná to náhoda.')
```
