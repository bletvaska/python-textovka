# Parse Line

## Čo je to parser?

Parser je rozpoznávač. V našom prípade bude rozpoznávať, aký príkaz hráč zadal z príkazového riadku.

Praser implementujeme vo forme funkcie, ktorej posunieme vstup od používateľa a ona nám vráti objekt daného príkazu. Ak
daný príkaz neexistuje, vráti nám hodnotu `None` alebo vyvolá výnimku.

## Parametre funkcie

Vytvoríme teda funkciu `parse_line()`, ktorá bude mať tieto parametre:

* `line` - vstup od používateľa
* `commands` - zoznam existujúcich príkazov

Funkcia vráti inštanciu príkazu (typu `Command`) alebo nevráti nič (hodnotu `None`, ktorá bude znamenať, že tento príkaz
parser nepozná). V prípade dohody môže funkcia vyvolať výnimku, ak nepozná daný príkaz.

Kostra funkcie môže vyzerať takto:

```python
def parse_line(line, commands):
   return None
```

## Type Hinting

Python je dynamický jazyk. To znamená, že interpreter bude vedieť, akého typu je daný parameter až v momente, keď sa
daný kód bude vykonávať.

To ale pre nás programátorov nie je veľmi výhodné, pretože nebudeme vedieť využívať výhody vývojového prostredia v
podobe intellisence (napr. automagické dopĺňanie syntaxe). Jednoducho si to môžete vyskúšať napísaním parametra
funkcie `line` na nový riadok v tele funkcie, za ním napísať operátor `.` a neuvidíte v zozname žiadnu metódu
typu `str`. To preto, že vývojové prostredie netuší, akého typu bude tento parameter.

```python
def parse_line(line: str, commands: list[Command]) -> Command | None:
   return None
```

* type hinting
   * parametre funkcie
   * navratovy typ
* predvoleny `return None` na konci
* `command.param`

```python
def parse_line(line: str, commands: list[Command]) -> Command | None:
   for command in commands:
      if line.startswith(command.name):
         command.param = line.split(command.name, maxsplit=1)[1].lstrip()
         return command

   return None  # default
```
