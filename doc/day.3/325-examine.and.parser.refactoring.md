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

Kostra príkazu bude vyzerať nasledovne:

```python
class Examine(Command):
   name = 'preskumaj'
   description = 'zobrazí informácie o zvolenom predmete'

   def exec(self, room):
      print('skumam predmet')
```

Nezabudnúť ju pridať aj do zoznamu príkazov.

## Rozpoznávanie príkazov s parametrom

Náš parser momentálne dokáže rozpoznávať len príkazy, ktoré nemajú parameter. Aby sme mohli pracovať s príkazmi, ktoré
majú parameter, musíme ho upraviť. Ak totiž teraz napíšeme príkaz `preskumaj`, vypíše sa pomocná správa. Ak však
napíšeme príkaz `preskumaj bic`, dostaneme odpoveď, že hra daný príkaz nepozná.

Pri rozpoznávaní príkazov teda nemôžeme očakávať jeho presné znenie, ale budeme čakať, že vstup od používateľa sa bude
začínať názvom príkazu. To vieme overiť volaním metódy `.startswith()` (alebo aj metódy `.index()`) nad reťazcom so
vstupom od používateľa:

```python
>>> 'preskumaj bic'.startswith('preskumaj')
True
>>> 'preskumaj bic'.startswith('o hre')
False
```

Aktualizujeme teda parser nasledovne:

```python
def parse_line(line: str, commands: list[Command]) -> Command | None:
    for command in commands:
        if line.startswith(command.name):
            return command
    return None
```

Všetko funguje tak, ako doteraz a ako bonus parser teraz rozpozná aj príkaz `preskumaj` s parametrom.

## Parameter príkazu

Potrebujeme však ešte získať parameter, ktorým je názov predmetu, a ktorý je zadaný za príkazom.

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
