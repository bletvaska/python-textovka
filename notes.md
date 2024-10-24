# Main Building Blocks

* prikazy
* miestnost
* predmet
* kontext


## Miestnost

* opis
* zoznam predmetov
* zoznam vychodov z miesnosti
* meno


## Predmet

* vlastnosti (viem zobrat, viem preniest, da sa pouzit, ...)
* opis
* meno


## Prikaz

* meno
* opis
* pouzitie/spustenie
* [aliasy]

class Command:
   name: str
   description: str
   aliases: list

   def exec():
      pass



## Class

