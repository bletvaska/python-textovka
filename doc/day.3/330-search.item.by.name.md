# Vyhľadanie predmetu podľa mena

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
