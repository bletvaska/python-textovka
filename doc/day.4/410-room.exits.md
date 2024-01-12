# Východy z miestnosti

* ako slovník


## Modul `rooms.directions`

V tomto module zadefinujeme smery, ktorými môže Indy chodiť:

```python
NORTH = 90
SOUTH = 180
EAST = 0
WEST = 270
UP = -90
DOWN = -180

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
# show exits from room
if len(self.exits) == 0:
   print('Z miestnosti nevedú žiadne východy.')
else:
   directions = []

   if NORTH in self.exits:
       directions.append('sever')
   if SOUTH in self.exits:
       directions.append('juh')
   if EAST in self.exits:
       directions.append('východ')
   if WEST in self.exits:
       directions.append('západ')
   if UP in self.exits:
       directions.append('hore')
   if DOWN in self.exits:
       directions.append('dolu')

   print('Možné východy z miestnosti:')
   for direction in directions:
       print(f'* [bold yellow]{direction}[/bold yellow]')
```
