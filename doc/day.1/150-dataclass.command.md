# Command Dataclass

## Module `commands.py`

* vytvoríme samostatný modul s názvom `commands.py`, do ktorého presunieme implementáciu všetkých príkazov


## Command Dataclass

```python
from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic game command.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self):
        print('vykonavam prikaz ', self.name)
```
