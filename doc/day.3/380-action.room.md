# Action Room

## Problém

Niekoľko miestností v hre vyžaduje špeciálnu aktivitu bez toho, aby hráč urobil nejakú interakciu navyše. Napríklad:

* Ak Indy včas neopustí lietadlo, havaruje.
* Ak Indy včas neotvorí padák, zabije sa.
* Ak Indy nebude mať oblečenú uniformu, zastrelí ho stráž.

## Rozsirenie triedy `Room` o metodu `.act()`

Do triedy `Room` vložíme špeciálnu metódu `.act()`, ktorá sa spustí po vykonaní každého príkazu. Táto metóda nebude
robiť nič (v tele bude mať prázdny príkaz `pass`). V prípade, že si špeciálnu činnosť bude miestnosť vyžadovať, túto
špeciálnu funkcionalitu v triede reprezentujúcej konrétnu miestnosť implementujeme.

Metóda `.act()` bude obsahovať parameter typu `GameContext`, pretože po jej vykonaní sa môže zmeniť stav celej hry (
najčastejšie môže Indy zomrieť, čím sa hra ukončí).

Metóda v triede `Room` bude teda vyzerať nasledovne:

```python
def act(self, context):
   pass
```

Jej pravidelné spúšťanie zabezpečíme v hernej slučke rovno po spustení príkazu zadaného hráčom:

```python
 # parse and execute command
command = parse_line(line, context.commands)
if command is None:
   print('Taký príkaz nepoznám.')
else:
   command.exec(context)
   context.current_room.act(context)
```


## Trieda `InPlane`

```python
import states
from context import Context
from rooms import Room


class InPlane(Room):
   steps = 3

   def act(self, context: Context):
      # decrease nr of steps
      if self.steps != 0:
         self.steps = self.steps - 1
         return

      # death of indiana jones
      print('Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana '
            'Jones nemohol prežiť podobnú radostnú udalosť.')

      context.game_state = states.PLANE_CRASH
```
