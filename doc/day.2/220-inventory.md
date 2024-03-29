# Príkaz `inventar`

## Ciele

1. Naučiť sa odovzdávať dáta funkciám/metódam pomocou parametrov

V module `commands.py` vytvorte triedu `Inventory`, ktorá bude reprezentovať príkaz `inventar` na výpis obsahu batohu. O
príkaze bude platiť:

* jeho meno je `inventar`
* jeho opis je `zobrazí obsah hráčovho batohu`

V prípade, že je batoh prázdny, vypíše na obrazovku text:

```
Batoh je prázdny.
```

V opačnom prípade vypíše na obrazovku zoznam predmetov v batohu napríklad takto:

```
V batohu máš:
bic
```

**Poznámka:** Nezabudnite rozšíriť aj zoznam dostupných príkazov, ktorý sa zobrazí po zadaní príkazu `prikazy`.

### Kostra riešenia

```python
class Inventory(Command):
   name = 'inventar'
   description = 'zobrazí obsah hráčovho batohu'

   def exec(self):
      print('Obsah batohu.')
```

## Problém

Ako však dostať obsah premennej `backpack` z modulu `main` do metódy `.exec()` triedy `Inventory`, ktorá sa nachádza v
module `commands`?

Batoh odovzdáme ako parameter metódy `.exec()`:

```python
def exec(self, backpack):
    print(backpack)
```


## Riešenie

```python
class Inventory(Command):
   name = 'inventar'
   description = 'zobrazí obsah hráčovho batohu'

   def exec(self, backpack):
      # check if backpack is empty
      if len(backpack) == 0:  # backpack == []
         print('Batoh je prázdny')
         return

      # print content of backpack
      print('V batohu máš:')
      for item in backpack:
         print(item)
```


## Additional Tasks

1. Miesto výpisu predmetov pod seba ich vypíšte vedľa seba

   ```python
   def exec(self, backpack):
       if backpack == []:
           print("Batoh je prázdny.")
       else:
           print(f"V batohu mas: {', '.join(backpack)}")
   ```
