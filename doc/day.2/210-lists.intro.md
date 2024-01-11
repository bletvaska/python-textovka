# About Lists

## Goals

1. Naučiť sa základy práce so zoznamami

## The Problem

Hráč bude so sebou všade nosiť batoh, v ktorom bude môcť prenášať predmety. Bude ich vedieť do batohu vkladať, a rovnako
tak v ďalších miestnostiach vykladať. Inokedy bude potrebné v batohu potrebné nájsť potrebný predmet, lebo ho bude
potrebovať použiť.

Batoh v hre budeme reprezentovať pomocou zoznamu.

Naučiť sa pracovať so zoznamami je veľmi dôležité, pretože zoznamy patria k jedným z najčastejšie používaných dátových
týpov. Rovnako to bude aj v našom prípade - nepoužijeme ich len pri tvorbe batohu, ale aj pri zobrazovaní zoznamu
predmetov v miestnosti alebo pri rozpoznávaní/zobrazovaní príkazov, ktoré hráč môže v hre použiť.

Teraz si teda ukážeme základy práce so zoznamami.


## Lists 101

### Vytvorenie prazdneho batohu

```python
>>> bp = []
>>> type(bp)
list
```

### Vytvorenie neprazdneho batohu

```python
>>> bp = ['bic']
```

### Vlozenie novych veci do batohu

Do batohu postupne vlozime klobuk, revolver a mapu:

```python
>>> bp.append('klobuk')
>>> bp.append('revolver')
>>> bp.append('mapa')
```

Obsah batohu skontrolumeme:

```python
>>> bp
['bic', 'klobuk', 'revolver', 'mapa']
```

### Pocet prvkov v batohu

```python
>>> len(bp)
4
```

### Pristup ku jednotlivym prvkom

```python
>>> bp[0]
'bic'
```

### Slicing operator

```python
>>> bp[1:4]
['klobuk', 'revolver', 'mapa']
>>> bp[:4]
['bic', 'klobuk', 'revolver', 'mapa']
>>> bp[2:]
['revolver', 'mapa']
>>> bp[:]
['bic', 'klobuk', 'revolver', 'mapa']
>>> bp[::1]
['bic', 'klobuk', 'revolver', 'mapa']
>>> bp[::2]
['bic', 'revolver']
>>> bp[::-1]
['mapa', 'revolver', 'klobuk', 'bic']
```

### Prejst prvky jeden po druhom

```python
for item in bp:
   print(item)
```

### Zistit, ci je v batohu predmet

```python
>>> 'klobuk' in bp
True
```

### Najst predmet v batohu

```python
>>> bp.index('klobuk')
1
```

### Odstranit predmet z batohu

```python
>>> bp.remove('bic')
>>> bp
['klobuk', 'revolver', 'mapa']
```

```python
>>> bp.pop(2)
'mapa'
>>> bp
['klobuk', 'revolver']
```

```python
>>> bp.pop()
'revolver'
```

### Vlozit do batohu obsah ineho batohu

```python
>>> stash = ['diamant', 'kriz', 'minca']
>>> bp = bp + stash
>>> bp
['klobuk', 'diamant', 'kriz', 'minca']
```

### Zmenit predmet v batohu

```python
>>> bp[3] = 'zlata minca'
>>> bp
['klobuk', 'diamant', 'kriz', 'zlata minca']
```
