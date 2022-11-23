# Command Dataclass

```python
from dataclasses import dataclass


@dataclass
class Command:
    """
    Describes every command in game.
    """
    # fields
    name: str
    description: str

    # behavior / methods
    def exec(self, backpack):
        # ! FIXME exception
        print('vykonavam prikaz')
```
