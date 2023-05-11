# Color Output with rich

[![Logo modulu rich](../images/logo-rich.svg)](https://github.com/Textualize/rich)


## Inštalácia

Nainštalujeme

```bash
$ poetry add rich
```

alebo

```bash
$ pip install rich
```

## Použitie

Upravíme výpis názvu predmetu v príkaze `inventar`:

```python
print(f'  [bold magenta]{item.name}[/bold magenta]')
```

Musíme však najprv importovať funkciu `print` z modulu `rich`:

```python
from rich import print
```