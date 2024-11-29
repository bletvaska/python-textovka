# Príkaz reštart

Vytvorte príkaz `restart`, ktorý reštartuje hru (resetuje kontext hry).

O tomto príkaze platí, že:

* jeho definícia je v triede `Restart` v module `restart.py`, ktorý sa nachádza v balíku `commands`
* názov príkazu je `restart`
* opis príkazu je `reštartuje rozohratú hru`

Predtým, ako hru reštartujete, sa hráča pre istotu opýtajte, či chce hru naozaj reštartovať zavolaním funkcie
`ask_yes_no()`. V prípade, že odpovie kladne, hru reštartujte resetovaním kontextu.


## Riešenie

```python
class Restart(Command):
    name: str = 'restart'
    description: str = 'Restarts the adventure'

    def exec(self, context):
        answer = ask_yes_no('Naozaj chceš reštartovať rozohratú hru? ')
        if answer == True:
            context.reset()
            context.current_room.show()
```
