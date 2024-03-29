# Parse Line

## Čo je to parser?

Parser je rozpoznávač. V našom prípade bude rozpoznávať, aký príkaz hráč zadal z príkazového riadku.

Praser implementujeme vo forme funkcie, ktorej posunieme vstup od používateľa a ona nám vráti objekt daného príkazu. Ak
daný príkaz neexistuje, vráti nám hodnotu `None` alebo vyvolá výnimku.

## Parametre funkcie

V module `helpers` teda vytvoríme funkciu `parse_line()`, ktorá bude mať tieto parametre:

* `line` - vstup od používateľa
* `commands` - zoznam existujúcich príkazov

Funkcia vráti inštanciu príkazu (typu `Command`) alebo nevráti nič (hodnotu `None`, ktorá bude znamenať, že tento príkaz
parser nepozná). V prípade dohody môže funkcia vyvolať výnimku, ak nepozná daný príkaz.

Kostra funkcie môže vyzerať takto:

```python
def parse_line(line, commands):
   pass
```

## Type Hinting

Python je dynamický jazyk. To znamená, že interpreter bude vedieť, akého typu je daný parameter až v momente, keď sa
daný kód bude vykonávať.

To ale pre nás programátorov nie je veľmi výhodné, pretože nebudeme vedieť využívať výhody vývojového prostredia v
podobe intellisence (napr. automagické dopĺňanie syntaxe). Jednoducho si to môžete vyskúšať napísaním parametra
funkcie `line` na nový riadok v tele funkcie, za ním napísať operátor `.` a neuvidíte v zozname žiadnu metódu
typu `str`. To preto, že vývojové prostredie netuší, akého typu bude tento parameter.

```python
def parse_line(line: str, commands: list[Command]):
   pass
```

## Návratový typ funkcie a type hinting

* navratovy typ
* predvoleny `return None` na konci

```python
def parse_line(line: str, commands: list[Command]) -> Command | None:
# return None
```

## Vytvorená funkcia `parse_line()`

* `command.param` ?

```python
def parse_line(line: str, commands: list[Command]) -> Command | None:
   for command in commands:
      if line == command.name:
         return command

   return None  # default
```

## Použitie parsera

Vytvorený parser môžeme použiť dvoma spôsobmi:

1. pomocou `if-else`
2. pomocou ošetrenia výnimky

Príklady oboch použití sa nachádzajú v ďalšom texte.

Je však potrebné spraviť refaktoring kvôli parametrom vo volaní metódy `.exec()`: Príkaz `inventar` potrebuje mať pri
volaní batoh. Príkaz `prikazy` potrebuje mať zoznam príkazov. Ostatné príkazy nepotrebujú nič. Aby sme ale zabezpečili
jednodtné správanie, a aby každý príkaz dostal presne to, čo potrebuje, budeme posielať všetkým príkazom všetky potrebné
parametre. Tie, ktoré ich potrebujú, ich použijú a tie, ktoré ich nepotrebujú, ich nepoužijú.

Za tým účelom je potrebné upraviť aj podobu metódy `.exec()` priamo v triede `Command`:

```python
def exec(self, backapck: list[str], commands: list[Command]):
    raise NotImplementedError('This method was not yet implemented.')
```

### Použitie parsera pomocou `if-else`

```python
command = parse_line(line, commands)
if command is None:
   print('Taký príkaz nepoznám.')
else:
   command.exec(backpack, commands)
```

### Použitie parsera pomocou ošetrenia výnimky

```python
try:
   command.exec(backpack, commands)
   command.exec()
except AttributeError:
   print('Taký príkaz nepoznám.')
```
