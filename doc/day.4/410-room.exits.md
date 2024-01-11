# Východy z miestnosti

* ako slovník


## Modul `rooms.directions`

V tomto module zadefinujeme smery, ktorými môže Indy chodiť:

```python
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
DOWN = 'down'
UP = 'up'
```


## Rozšírenie metódy `.show()`

Aktualizujte metódu `.show()` v triede `Room` tak, aby zobrazovala aj východy z danej miestnosti.

* Ak z miestnosti nebudu viesť žiadne východy, tak vypíšte na obrazovku správu:

   ```
   Z miestnosti nevedú žiadne východy.
   ```

* Ak z miestnosti bude viesť minimálne jeden východ, vypíšte na obrazovku:

   ```
   Možné východy z miestnosti:
   * sever
   * dolu
   ```

   **Poznámka**: Východy z miestnosti vypisujeme farbou `yellow`.


## Riešenie

```python
# list exits
if self.exits == {}:
   print('Z miestnosti nevedú žiadne východy.')
else:
   dirs = []
   if DOWN in self.exits:
       dirs.append('dolu')
   if UP in self.exits:
       dirs.append('hore')
   if NORTH in self.exits:
       dirs.append('sever')
   if SOUTH in self.exits:
       dirs.append('juh')
   if EAST in self.exits:
       dirs.append('východ')
   if WEST in self.exits:
       dirs.append('západ')

   # render
   print('Možné východy z miestnosti:')
   for d in dirs:
       print(f'  [bold yellow]{d}[/bold yellow]')
```
