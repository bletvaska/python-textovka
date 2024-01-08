# Prikazy ako datove triedy


## Prikaz `prikazy`

Príkaz `prikazy` zobrazí zoznam dostupných príkazov hry. Bude to akýsi pomocník určený hlavne pre nových hráčov, ktorý ešte úplne nevedia, aké príkazy môžu v hre používať.


```python
class Commands(Command):
    """
    List all the commands of the game.
    """
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self):
        print('V hre je možné použiť tieto príkazy:')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
```

