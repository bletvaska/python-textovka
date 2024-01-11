# Balik `commands`

## co su to baliky

```
commands/
├── about.py
├── command.py
├── commands.py
├── __init__.py
└── quit.py
```

## pouzitie baliku `commands`

mozeme do `__init__.py` vlozit importy:

```python
from .about import About
from .quit import Quit
from .commands import Commands
```

a tym padom mozeme importovat jednoduchsie v `game.py`

```python
from commands import About, Commands, Quit
```
