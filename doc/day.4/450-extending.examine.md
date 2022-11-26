# Pokročilé preskúmanie predmetu

Po preskúmaní prázdnych sedadiel spoza nich vypadne padák. Začneme teda tým, že vytvoríme padák, ktorý spoza nich
vypadne a potom zabezpečíme, aby ten padák po preskúmaní naozaj vypadol.


## Predmet padák

Vytvorte predmet padák.

```python
from dataclasses import dataclass, field

from adventure.items import MOVABLE, USABLE, EXAMINABLE
from adventure.items.item import Item


@dataclass
class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE])
```


## Preskúmateľné sedadlá

Vytvoríme dohodu, že predmety, ktoré sa budú dať preskúmať (to znamená, že medzi vlastnosťami budú mať vlastnosť
`EXAMINABLE`), budú mať vytvorenú metódu `examine()`. V tejto metóde bude uvedené, čo presne znamená preskúmať daný
predmet. No a túto metódu následne zavolá príkaz `preskumaj`. Ten si najprv overí, či uvedený predmet je
preskúmateľný a následne túto metódu nad predmetom zavolá.

Indiana Jones po preskúmaní sedadiel objaví padák. Ten sa samozrejme dostane do zoznamu predmetov v miestnosti.

Implementácia metódy `examine()` v predmete `prazdne sedadla` teda môže vyzerať takto:

```python
def examine(self, context):
   # add parachute to current room
   room = get_current_room(context)
   room.items.append(Parachute())

   # remove EXAMINABLE from list of features
   self.features.remove(EXAMINABLE)

   # render
   print('Pod jedným z nich si našiel padák. Šťastná to náhoda.')
```

**Poznámka:** Pre fajnšmekrov treba dodať, že toto nie je objektovo-orientované riešenie problému.


## Rozšírenie príkazu `preskumaj`
