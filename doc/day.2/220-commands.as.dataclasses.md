# Prikazy ako datove triedy

kazdy jeden prikaz bude potomkom triedy `Command`


## Prikaz `o hre`

```python
from dataclasses import dataclass

from .command import Command


@dataclass
class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, context, param):
        print('Hru Indiana Jones 2 napísal mladý nádejný programátor v jazyku Python - mirek v roku 2022.')
```

## Prikaz `prikazy`

```python
from dataclasses import dataclass

from .command import Command


@dataclass
class Commands(Command):
    # fields
    name: str = 'prikazy'
    description: str = 'zobrazí dostupné príkazy v hre'

    # methods
    def exec(self, context, param):
        print('V hre je možné použiť tieto príkazy:')

        for command in context.commands:
            print(f'* {command.name} - {command.description}')
```


## Prikaz `koniec`

```python
from dataclasses import dataclass

from states import STATE_QUIT
from .command import Command


@dataclass
class Quit(Command):
    # fields
    name: str = 'koniec'
    description: str = 'ukončí hru'

    # methods
    def exec(self, context, param):
        choice = input('Naozaj chceš ukončiť hru? (a/n) ').lstrip().rstrip().lower()
        if choice in ('y', 'yes', 'a', 'ano'):
            context.game_state = STATE_QUIT
```
