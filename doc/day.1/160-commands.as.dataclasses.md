# Príkazy ako dátové triedy

kazdy jeden príkaz bude potomkom triedy `Command`


## Príkaz `o hre`

```python
class About(Command):
    """
    Shows info about the game.
    """
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2023 created by mirek')
        print('Dalšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')
```


## Použitie príkazu

Pomocou tejto triedy sme uzavreli vlastnosti ako aj správanie do jedného celku s názvom trieda. Ak triedu budeme
chcieť použiť, budeme z nej musieť najprv vytvoriť objekt. To zabezpečíme volaním:

```python
about = About()
```

Následne môžeme nad vytvoreným objektom typu `About` zavolať metódu `.exec()`:

```python
about.exec()
```

To je samozrejme možné napísať aj v jednom riadku takto:

```python
About().exec()
```

Aktualizujeme teda pôvodný kód a hernú slučku, kde sa nachádza časť kódu, ktorá sa spustí v prípade napísania
príkazu `o hre`. Táto časť bude teraz vyzerať takto:

```python
elif line == 'o hre':
    About().exec()
```
