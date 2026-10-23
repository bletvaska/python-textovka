# Príkaz `koniec`

## Goals

1. Návratová hodnota funkcie/metódy.

## Vytvorenie príkazu `koniec`

Pomocou tohto príkazu ukončíme hru. Aby však nedošlo k ukončeniu omylom, pred ukončením sa hráča najprv opýtame, či chce
hru naozaj skončiť.

```python
class Quit(Command):
   name = 'koniec'
   description = 'ukončí rozohratú hru'

   def exec(self):
      choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
      if choice in ('ano', 'a', 'yes', 'y'):
         game_state = states.QUIT
```

Ak však tento príkaz spustíme a vyberieme si možnosť `ano`, hra sa žiaľ neukončí. Prečo?

Je to kvôli tomu, že premenná `game_state`, do ktorej ukladáme nový stav, je lokálnou premennou v metóde `.exec()`. Táto
premenná prestane existovať po ukončení metódy.


## Funkcie/metódy vracajúce hodnotu

Ak chceme zabezpečiť, aby sa hra ukončila, potrebujeme nový stav dostať z metódy `.exec()` von do miesta volania v
module `main.py`. Aktuálne to môžeme docieliť jedine tak, že nový stav vrátime z metódy `.exec()` ako návratovú hodnotu.
Ak chceme, aby funkcia/metóda niečo vrátila po ukončení svojej činnosti, použijeme na to príkaz `return`.

Metóda `.exec()` vracajúca nový stav bude vyzerať takto:

```python
def exec(self):
    choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
    if choice in ('ano', 'a', 'yes', 'y'):
        return states.QUIT
```

V module `main.py` upravíme fragment kódu, kde spúšťame príkaz `koniec` takto:

```python
elif line == 'koniec':
    cmd = Quit()
    game_state = cmd.exec()
```

Ak vyskúšame hru ukončiť, budeme úspešní. Ak však hráč napíš `nie`, hra sa ukončí aj tak. V čom je problém?

V implementácii metódy `.exec()` nemáme ošetrené to, čo metóda vráti, ak hráč vyberie opačnú voľbu, ako "áno". Naivne sa
teda môžeme domnievať, že sa pôvodná hodnota nezmení.

Python však v prípade, ak z funkcie neodídeme pomocou príkazu `return`, doplní na koniec riadok

```python
return None
```

To znamená, že aj keď sme explicitne neuviedli návratovú hodnotu z metódy, funkcia vráti hodnotu `None`. Aby to tak
nebolo, v prípade, že hráč bude chcieť v hre pokčačovať, explicitne vrátime stav `status.PLAYING`.

Metódu `.exec()` upravíme nasledovne:

```python
def exec(self):
   choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
   if choice in ('ano', 'a', 'yes', 'y'):
      return states.QUIT

   return states.PLAYING
```
