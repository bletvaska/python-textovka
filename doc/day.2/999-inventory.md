# Inventory

Batoh a príkaz inventár. Práca so zoznamami, formátovanie reťazcov.

## Goals

1. Naučiť sa základy práce so zoznamami
2. Naučiť sa formátovať reťazce pomocou (f-strings)

## The Backpack

1. Vytvorte hráčov batoh (inventár), v ktorom bude hráč môcť prenášať predmety medzi miestnosťami. Batoh reprezentuje ako zoznam a uložte ho do premennej `backpack`.

    ```python
    backpack = []
    ```

    Pre testovacie účely ho môžete v prípade potreby naplniť nejakými predmetmi, ktoré bude mať hráč v batohu rovno po spustení:

    ```python
    backpack = [ 'bic', 'revolver' ]
    ```

    ukazka prace so zoznamami

    * pocet prvkov `len(items)`
    * pristup ku jednotlivym prvkom `items[0]`
    * slicing operator
    * prejst prvky jeden po druhom
    * vlozit nieco do zoznamu
    * najst nieco v zozname
    * opýtať sa, či sa niečo v zozname nachádza cez operátor `in`
    * odstranit nieco zo zoznamu
    * rozsirit zoznam o iny zoznam
    * zmenit prvok zoznamu


2. Vytvorte príkaz `inventar`, ktorý vypíše obsah batohu. Príkaz `inventar` bude mať aliasy `inventory` a `i`. V prípade, že je batoh prázdny, vypíše na obrazovku text:

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
   elif line == 'inventar':
       if backpack == []:  # len(backpack) == 0
           print("Batoh je prázdny.")
       else:
           print("V batohu máš:")
           for item in backpack:
               print(f'* {item}')
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
