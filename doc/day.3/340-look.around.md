# Príkaz `Rozhliadni sa` a aktuálna miestnosť

## Lab

V module `look_around.py` vytvorte triedu `LookAround`, ktorá bude reprezentovať príkaz `rozhliadni sa`. Vlastnosti
tohto príkazu sú:

* názov - `rozhliadni sa`
* opis - `rozhliadne sa v aktuálnej miestnosti`

Po zadaní tohto príkazu sa zobrazí opis miestnosti. To znamená, že nad objektom aktuálnej miestnosti sa zavolá
metóda `.show()`.


## Riešenie

```python
class LookAround(Command):
   name: str = 'rozhliadni sa'
   description: str = 'rozhliadne sa v aktuálnej miestnosti'

   def exec(self, context):
      context.current_room.show()
```
