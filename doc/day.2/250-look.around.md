# Príkaz Rozhliadni sa

Vytvorte príkaz `rozhliadni sa`. Vlastnosti tohto príkazu sú:

* názov - `rozhliadni sa `
* opis - `rozhliadne sa v aktuálnej miestnosti`

Po zadaní tohto príkazu sa znovu zobrazí opis miestnosti spolu so zoznamom predmetov, ktoré sa v nej nachádzajú.

Po vytvorení príkazu nezabudnite aktualizovať zoznam príkazov hry, ktorý je dostupný po zadaní príkazu `prikazy`.

```
> rozhliadni sa
Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že áno?)
Vidíš:
  bič
  prázdne sedadlá
```

## Pokus o riešenie

```python
class LookAround(Command):
   name = 'rozhliadni sa'
   description = 'rozhliadne sa v aktuálnej miestnosti'

   def exec(self):
      print(current_room.description)
      print('Vidíš:')
      for item in current_room.items:
          print(item)
```

Lenže nebude fungovať, pretože premenná `current_room` nie je v tomto kontexte definovaná.

## Metóda `.exec()` s parametrom

Aby príkaz fungoval, ako mal, musíme miestnosť do príkazu dostať. Do metódy `.exec()` preto pridáme parameter `room`:

```python
class LookAround(Command):
   name = 'rozhliadni sa'
   description = 'rozhliadne sa v aktuálnej miestnosti'

   def exec(self, room):
      print(room.description)
      print('Vidíš:')
      for item in room.items:
          print(item)
```

## Refaktoring

Táto zmena sa však dotkne viacerých miest. V module `main` napríklad musíme tento parameter posunúť do metódy `.exec()`
už pri jej volaní:

```python
# parse and execute command
command = parse_line(line, commands)
if command is None:
   print('Taký príkaz nepoznám.')
else:
   command.exec(current_room)
```

Ak by sme teraz spustili hru a napísali príkaz `rozhliadni sa`, tak všetko bude pracovať, ako má. Ak však napíšeme
akýkoľvek iný príkaz, skončíme s výnimkou. To preto, že parameter `room` používame pri každom jednom volaní
metódy `.exec()`. To znamená, že ho voláme pri každom jednom príkaze.

Tento problém potrebujeme vyriešiť na viacerých miestach:

* v triede `Command`
* v metóde `.exec()` každého jedného príkazu
