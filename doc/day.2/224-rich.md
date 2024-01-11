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

## Použitie vo výpise predmetov v príkaze `inventar`

Upravíme výpis názvu predmetu v príkaze `inventar`:

```python
print(f'  [bold magenta]{item}[/bold magenta]')
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



## Problém v prostredí PyCharm

Ak program spúšťate v prostredí PyCharm, pravdepodobne výstup fialový neuvidíte. Aby ste ho videli, tak potrebujete
urobiť toto:

1. `Run > Edit Configurations...`
2. vyberte si spúšťač, pomocou ktorého spúšťate hru
3. rozlikliknite `Modify options` a vyberte voľbu `Emulate terminal in output console`
4. potvrďte zmeny kliknutím na tlačidlo `OK`

Keď teraz hru spustíte, zoznam predmetov už bude fialový.
