# Parse Line

* type hinting
  * parametre funkcie
  * navratovy typ
* predvoleny `return None` na konci
* `command.param`

```python
def parse_line(line: str, commands: list[Command]) -> Command | None:
    for command in commands:
        if line.startswith(command.name):
            command.param = line.split(command.name, maxsplit=1)[1].lstrip()
            return command

    return None  # default
```
