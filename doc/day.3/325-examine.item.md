# Príkaz `preskumaj`

Vytvorte príkaz `preskumaj`, pomocou ktorého zobrazíte opis predmetu, ktorý sa musí nachádzať v miestnosti.

O príkaze bude platiť:

* meno príkazu - `preskumaj`
* opis príkazu - `zobrazí informácie o zvolenom predmete`

O jeho správaní bude platiť nasledovné:

* Ak predmet nebol v príkaze uvedený, vypíšte na obrazovku správu:

   ```
   > preskumaj
   Neviem, čo chceš preskúmať.
   ```

* Ak hráč napíše názov predmetu, ktorý sa v miestnosti nenachádza, vypíšte na obrazovku správu:

   ```
   > preskumaj elektricka
   Taký predmet tu nikde nevidím.
   ```

* Ak hráč napíše názov predmetu, ktorý sa v miestnosti nachádza, tak na obrazovku vypíšte jeho opis

   ```
   > preskumaj bic
   Tvoj neoceniteľný pomocník..!
   ```


## Riešenie

```python
class Examine(Command):
   name = 'preskumaj'
   description = 'zobrazí informácie o zvolenom predmete'

   def exec(self, context):
      # if no item was entered
      if self.param == '':
         print('Neviem, čo chceš preskúmať.')

      # search for item
      else:
         # search for item in backpack
         for item in context.backpack:
            if item.name == self.param:
               print(item.description)
               break
         else:
            # search for item in current room
            for item in context.current_room.items:
               if item.name == self.param:
                  print(item.description)
                  break
            else:
               # not found
               print('Taký predmet tu nikde nevidím.')

```
