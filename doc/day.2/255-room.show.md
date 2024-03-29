# Rozhliadnutie sa v miestnosti

## Aktualizácia triedy `Room`

V triede `Room` vytvorte metódu `.show()`, pomocou ktorej "vykreslíte" obsah miestnosti na obrazovku.

```python
from pydantic import BaseModel


class Room(BaseModel):
    # fields
    name: str
    description: str
    items = []  # : list
    exits = []  #: list

    def show(self):
        """
        Shows the current room.
        """
        print(self.description)
        print('Vidíš:')
        for item in self.items:
            print(item.name)
```


## Aktualizácia príkazu `rozhliadni sa`

```python
class LookAround(Command):
    name = 'rozhliadni sa'
    description = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, room):
        room.show()

        return states.PLAYING
```
