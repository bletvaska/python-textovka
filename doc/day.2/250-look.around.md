# Príkaz `Rozhliadni sa` a aktuálna miestnosť

## Lab

V module `look_around.py` vytvorte triedu `LookAround`, ktorá bude reprezentovať príkaz `rozhliadni sa`. Vlastnosti tohto príkazu sú:

* názov - `rozhliadni sa`
* opis - `rozhliadne sa v aktuálnej miestnosti`

Po zadaní tohto príkazu sa zobrazí opis miestnosti. To znamená, že nad objektom aktuálnej miestnosti sa zavolá metóda `.show()`.


## Problém: ako získať aktuálnu miestnosť?

Ak sa nad tým zamyslíme, tak prídeme na to, že pri volaní príkazu nemáme k dispozícii aktuálnu miestnosť. Ak teda chceme úlohu splniť, musíme pred vytvorením príkazu aktualizovať herný kontext a rozšíriť ho o aktuálnu miestnosť:

```python
class GameContext(BaseModel):
    backpack: list = []
    commands: list[Command] = []
    game_state: str = PLAYING
    current_room: Room = None
```

Vzhľadom na úpravu kontextu je potrebné urobiť aj jemný refaktoring celého kódu a teda najmä začiatku hry v module `main.py`

* je potrebné aktualizovať vytvorenie kontextu pridaním aktuálnej miestnosti
* je potrebné upraviť prvotné zobrazenie miestnosti, v ktorej sa Indiana Jones nachádza po spustení hry


## Riešenie

```python
class LookAround(Command):
   name = 'rozhliadni sa'
   description = 'rozhliadne sa v aktuálnej miestnosti'

   def exec(self, context):
      context.current_room.show()
```
