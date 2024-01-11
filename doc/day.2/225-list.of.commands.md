# Zoznam príkazov

Máme vytvorený batoh, ktorý pozostáva zo zoznamu predmetov, teraz môžeme vytvoriť zoznam dostupných príkazov v
hre.

```python
commands = [
   About(),
   Commands(),
   Inventory(),
   Quit(),
]
```

Vďaka tomu môžeme príkazy zobrazovať dynamicky - tento zoznam posunieme ako parameter metóde `.exec()`
príkazu `Commands` a názov každého jedného vypíšeme farbou `cyan`:

```python
def exec(self, commands):
   print('V hre je možné použiť tieto príkazy:')

   for command in commands:
      print(f'* [bold cyan]{command.name}[/bold cyan] - {command.description}')
```


## Additional topics

Zoznam príkazov je možné vypísať aj zotriedene.

* metóda `.sort()` nad zoznamom
  * vie pracovať nad základnými typmi (čísla, reťazce, ...)
  * nevie pracovať s triedami (na základe čoho bude vedieť, že jeden príkaz má byť v poradí pred druhým?)
* je potrebné implementovať magic/dunder metódy `__eq__()`, `__lt__()` a `__gt__()`

```python
 def __eq__(self, other):
     return self.name == other.name

 def __lt__(self, other):
     return self.name < other.name

 def __gt__(self, other):
     return self.name > other.name
```

Potom je možné zoznam zotriediť zavolaním metódy `.sort()` nad zoznamom príkazov:

```python
commands.sort()
```
