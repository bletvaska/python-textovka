# Príkaz `inventar`

Vytvorte príkaz `inventar`, ktorý vypíše obsah batohu. V prípade, že je batoh prázdny, vypíše na obrazovku text:

```
Batoh je prázdny.
```

V opačnom prípade vypíše na obrazovku zoznam predmetov v batohu napríklad takto:

```
V batohu máš:
* bic
* revolver
```

**Poznámka:** Nezabudnite rozšíriť aj zoznam dostupných príkazov, ktorý sa zobrazí po zadaní príkazu `prikazy`.

```python
from .command import Command


class Inventory(Command):
    name = 'inventar'
    description = 'zobrazí obsah hráčovho batohu'

    def exec(self, context) -> str:
        # check if backpack is empty
        if len(context.backpack) == 0:  # context.backpack == []
            print('Batoh je prázdny')
            return

        # print content of backpack
        print('V batohu máš:')
        for item in context.backpack:
            print(f'  {item.name}')
```



### Additional Tasks

1. Miesto výpisu predmetov pod seba ich vypíšte vedľa seba

   ```python
   elif line in ("inventar", 'inventory', 'i'):
       if backpack == []:
           print("Batoh je prázdny.")
       else:
           print(f"V batohu mas: {', '.join(backpack)}")
   ```