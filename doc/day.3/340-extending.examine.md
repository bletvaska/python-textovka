# Pokročilé preskúmanie predmetu

Po preskúmaní prázdnych sedadiel spoza nich vypadne padák. Začneme teda tým, že vytvoríme padák, ktorý spoza nich
vypadne a potom zabezpečíme, aby ten padák po preskúmaní naozaj vypadol.


## Predmet padák

Vytvorte predmet padák.

```python
from items.features import MOVABLE, USABLE, EXAMINABLE
from items.item import Item


class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features = [MOVABLE, USABLE]
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

```python
 def exec(self, context):
     if self.param == '':
         print('Neviem, čo chceš preskúmať.')
     else:
         for item in context.current_room.items:
             if item.name == self.param:
                 print(item.description)

                 # is item examinable?
                 if EXAMINABLE in item.features:
                     input('Skúmam...')
                     item.examine(context)

                 return

         print('Taký predmet tu nikde nevidím.')
```
