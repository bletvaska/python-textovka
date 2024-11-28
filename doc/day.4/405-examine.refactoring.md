# Refaktoring príkazu preskumaj

Vytvorili sme funkciu `search_item_by_name()`, ktorá nám uľahčí tvorbu funkcií, kde potrebujeme zistiť, či sa niektorý predmet nachádza v miestnosti alebo v zozname. To vieme okamžite využiť v implementácii príkazu `preskumaj`, kde aktuálne prehľadávame zoznam predmetov v miestnosti ručne. Úprava metódy `exec` bude vyzerať nasledovne:


```python
 def exec(self, context):
     item_name = self.param

     # if not item was entered
     if item_name == '':
         print('Neviem, čo chceš preskúmať.')
         return

     # if not found
     item = get_item_by_name(item_name, context.current_room.items)
     if item is None:
         print('Taký predmet tu nikde nevidím.')
         return

     # when found
     print(item.description)
```
