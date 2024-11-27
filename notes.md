# Main Building Blocks

* prikazy
* miestnost
* predmet
* kontext hry


## Miestnost

* opis
* zoznam predmetov
* zoznam vychodov z miesnosti
* meno


## Predmet

* vlastnosti (viem preniest, da sa preskumat, da sa pouzit, ...)
* opis
* meno


## Prikaz

* meno
* opis
* pouzitie/spustenie
* [aliasy]

```python
class Command:
   name: str
   description: str
   aliases: list

   def exec(self):
      pass
```



## Kontext hry

* batoh
* zoznam prikazov
* aktualna miestnost
* zoznam vsetkych miestnosti
* historia prikazov
* stav hry
