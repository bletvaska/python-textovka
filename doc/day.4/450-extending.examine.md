# Preskúmateľné sedadlá

Vytvoríme dohodu, že predmety, ktoré sa budú dať preskúmať (to znamená, že medzi vlastnosťami budú mať vlastnosť
`EXAMINABLE`), budú mať vytvorenú metódu `examine()`. V tejto metóde bude uvedené, čo presne znamená preskúmať daný
predmet. No a túto metódu následne zavolá príkaz `preskumaj`. Ten si najprv overí, či uvedený predmet je
preskúmateľný a následne túto metódu nad predmetom zavolá.

Indiana Jones po preskúmaní sedadiel objaví padák. Ten sa samozrejme dostane do zoznamu predmetov v miestnosti.

Implementácia metódy `examine()` v predmete `prazdne sedadla` teda môže vyzerať takto:

```python
def examine(self, context):
   # add parachute to current room
   context.current_room.items.append(Parachute())

   # remove EXAMINABLE from list of features
   self.features.remove(EXAMINABLE)

   # render
   print('Pod jedným z nich si našiel [bold magenta]padák[/bold magenta]. Šťastná to náhoda.')
```

**Poznámka:** Pre fajnšmekrov treba dodať, že toto nie je objektovo-orientované riešenie problému.


## Rozšírenie príkazu `preskumaj`

```python
 def exec(self, context, param):
     if param == '':
         print('Neviem, čo chceš preskúmať.')
         return

     item = get_item_by_name(param, context.current_room.items + context.backpack)
     if item is None:
         print('Taký predmet tu nikde nevidím.')
         return

     # action
     print(item.description)

     # is item examinable?
     if EXAMINABLE in item.features:
         input('Pozrel si sa trošku bližšie a...')
         item.examine(context)
```
