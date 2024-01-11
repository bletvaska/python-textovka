# Predmety v miestnosti

Vytvorené predmety vložte do miestnosti:

```python
Room(
        name='v lietadle',
        description='Prebudil si sa v malom dvojmotorovom lietadle, plachtiacom nad egyptskou púšťou. Je tu nádherný '
                    'kľud, pretože motory stoja a na palube nie je okrem teba živá duša. (Celkom zaujímavá situácia, '
                    'že?) ',
        items=[Whip(), EmptySeats()]
    ),
```

## Aktualizácia metódy `.show()`

Upravte metodu `Room.show()` tak, aby zobrazila aj predmety, ktore sa nachadzaju v miestnosti. Musi platit, ze:

* ak sa v miestnosti nenachadza ziadny predmet, tak vypisete na obrazovku retazec:

   ```
   Nevidíš tu nič zvláštne.
   ```

* ak sa v miestnosti nejake predmety nachadzaju, tak ich vypisete v tvare:

   ```
   Vidíš:
   * bic
   * prazdne sedadla
   ```

## Riešenie

```python
def show(self):
    """
    Shows the current room.
    """
    print(self.description)
    if self.items != []:  # len(current_room.items) > 0
        print('Vidíš:')
        for item in self.items:
            print(f'  {item}')
    else:
        print('Nevidíš tu nič zvláštne.')
```
