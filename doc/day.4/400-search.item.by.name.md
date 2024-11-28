# Vyhľadanie predmetu podľa mena

V našom kóde v implementácii príkazu `preskumaj` si ručne vyhľadávame, či sa predmet nachádza v miestnosti. Podobnú
funkcionalitu však budeme používať aj v ďalších príkazoch:

* `vezmi` - budeme hľadať predmet v miestnosti
* `poloz` - budeme hľadať predmet v batohu
* `pouzi` - budeme hľadať predmet v batohu

Uvedená funkcionalita sa teda bude opakovať. Keďže sa snažíme dodržiavať princíp _DRY_, vytvoríme si samostatnú
funkciu `get_item_by_name()`, ktorej úlohou bude nájsť predmet na základe mena v zozname predmetov.

Vďaka tejto funkcii sa nám aj výsledný kód zjednoduší a sprehľadní hlavne vtedy, ak aplikujeme _Guard Clause_.
Výsledný kód sa nám tým pádom ani veľmi nebude hniezdiť dovnútra.


## Lab

Vytvorte funkciu `get_item_by_name()`, ktorá vyhľadá predmet v zozname na základe jeho názvu.

Funkcia bude mať tieto dva parametre:

* `name` - názov predmetu, ktorý chceme nájsť
* `items` - zoznam predmetov, v ktorom chceme predmet nájsť

Funkcia vráti objekt typu `Item`, ktorý reprezentuje daný predmet, ak sa jej ho podarilo v uvedenom zozname podľa
mena nájsť. V opačnom prípade vráti hodnotu `None`.

Funkciu umiestnite do modulu `helpers`.


```python
def get_item_by_name(name: str, items: list[Item]) -> Item | None:
    pass
```


## Riešenie

```python
def get_item_by_name(name: str, items: list[Item]) -> Item | None:
   """
   Return item by its name or None if not found.
   """
    for item in items:
        if item.name == name:
            return item

    # return None  # default
```
