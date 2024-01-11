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
