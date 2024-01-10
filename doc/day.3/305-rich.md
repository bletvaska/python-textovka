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

## Použité farby v hre

V hre budeme používať tieto farby:

* názov predmetu - `magenta`
* smer z miestnosti - `yellow`
* názov miestnosti - `green`

## Refaktoring

Pre použitie farieb v hre aktuálne stačí upraviť len metódu `.show()` v triede `Room`, kde dochádza k výpisovaniu názvov
predmetov.

```python
def show(self):
    print(self.description)
    print()

    if len(self.items) != 0:  # self.items != []
        print('Vidíš:')
        for item in self.items:
            print(item.name)
    else:
        print('Nevidíš tu nič zvláštne.')
```
