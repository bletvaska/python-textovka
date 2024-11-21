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
command, param = parse_line(line, context.commands)
if command is None:
    print('Taký príkaz nepoznám.')
else:
    command.exec(backpack)
    context.current_room.act(context)
```

## Trieda `Plane`

```python
class Plane(Room):
   name: str = 'lietadlo'
   description: str = 'Prebudil si sa v [bold green]malom dvojmotorovom lietadle[/bold green] plachtiacom nad '
                      'egyptskou púšťou. Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem '
                      'teba živej duše. (Celkom zaujímavá situácia, že áno?)'
   items: list[Item] = [
      Whip(),
      EmptySeats()
   ]
   exits: list = ['dolu']
```

### Aktualizácia herného kontextu

aktualizujeme herný kontext v module `main` alebo priamo triedu `GameContext` tak, že jej nastavíme ako prvú miestnosť práve lietadlo.

```python
context.current_room = Plane()
```


### Metóda `.act()`

Implementujte metódu `.act()` v miestnosti `Plane`. Zabezpečte, aby sa hra skončila, ak hráč zadá viac príkazov, ako
_4_.
V prípade, že sa hra skončí, tak:

   * vypíšte na obrazovku správu:

     `Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana Jones nemohol prežiť podobnú radostnú udalosť.`

   * zmeňte stav hry na hodnotu `PLANE_CRASH`

```python
class Plane(Room):
    name: str = 'lietadlo'
    description: str = 'Prebudil si sa v [bold green]malom dvojmotorovom lietadle[/bold green] plachtiacom nad ' \
                       'egyptskou púšťou. Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem ' \
                       'teba živej duše. (Celkom zaujímavá situácia, že áno?)'
    items: list[Item] = [
        Whip(),
        EmptySeats()
    ]
    exits: list = ['dolu']
    steps: int = 5

    def act(self, context):
      # decrease nr of steps
      if self.steps != 0:
         self.steps = self.steps - 1
         return

      # death of indiana jones
      print('Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana '
            'Jones nemohol prežiť podobnú radostnú udalosť.')

      context.game_state = states.PLANE_CRASH
```
