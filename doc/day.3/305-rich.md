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

Najprv nezabudnite importnúť funkciu `print()` z balíka `rich`:
```python
from rich import print
```

Následne aktualizjte výpis predmetov vo funkcii `.show()`:

```python
def show(self):
   print(self.description)
   print()

   if len(self.items) != 0:  # self.items != []
      print('Vidíš:')
      for item in self.items:
         print(f'* [bold magenta]{item.name}[/bold magenta]')
   else:
      print('Nevidíš tu nič zvláštne.')
```

## Problém v prostredí PyCharm

Ak program spúšťate v prostredí PyCharm, pravdepodobne výstup fialový neuvidíte. Aby ste ho videli, tak potrebujete
urobiť toto:

1. `Run > Edit Configurations...`
2. vyberte si spúšťač, pomocou ktorého spúšťate hru
3. rozlikliknite `Modify options` a vyberte voľbu `Emulate terminal in output console`
4. potvrďte zmeny kliknutím na tlačidlo `OK`

Keď teraz hru spustíte, zoznam predmetov už bude fialový.
