# Raising an Exception

## Problem

V podstate nám nič nebráni v tom, aby sme vytvorili aj inštanciu triedy `Command`, ktorá je predkom pre všetky príkazy.
To vieme zabezpečiť takto:

```python
command = Command()
```

Čo sa však stane po spustení príkazu - po zavolaní metódy `.exec()`?

Pragmatická odpoveď by mohla byť tá, že sa vykoná to, čo je v metóde zapísané.

V skutočnosti je ale odpoveď komplikovanejšia. Odpoveď na otázku "Čo sa stane po spustení príkazu?" je rovnaká, ako keby
sme sa mali opýtať "Akej farby je auto?" alebo "Ako chutí ovocie?". Nevieme totiž, aký príkaz
spúšťame (`o hre`? `prikazy`? `koniec`?) alebo o akom aute hovoríme alebo do akého ovocia sme sa práve zahryzli?

Logickejšie by bolo, aby sme nedovolili vytvoriť inštanciu z triedy `Command`, ktorá len opisuje príkaz vo všeobecnosti.
Alebo aby nešlo spustiť metódu `.exec()`.

"Zakázať" vykonanie metódy `.exec()` môžeme aj ináč - ak sa niekto pokúsi túto metódu zavolať, vyvoláme výnimku. A
pokiaľ výnimka nebude ošetrená, program sa ukončí. V podstate budeme upozornení na to, že implementácia metódy `.exec()`
neexistuje. Alebo sme ju zabudli napísať, ak sme vytvorili vlastnú triedu, ktorá je potomkom triedy `Command`, ale
zabudli sme implementovať metódu `.exec()`.

S týmto mechanizmom sa dá stretnúť často.

## What is an Exception?



```python
class Command(BaseModel):
   name: str
   description: str

   def exec(self):
      raise NotImplementedError('This method was not yet implemented.')
```
