# Balik `commands`

co su to baliky

```
commands/
├── about.py
├── command.py
├── commands.py
├── __init__.py
├── look_around.py
└── quit.py
```

mozeme do `__init__.py` vlozit importy:

```python
from .about import About
from .look_around import LookAround
from .quit import Quit
from .commands import Commands
```

a tym padom mozeme importovat jednoduchsie v `game.py`

```python
from commands import About, Commands, Quit, LookAround
```
