# Refaktoring príkazu preskumaj

Vytvorili sme funkciu `search_item_by_name()`, ktorá nám uľahčí tvorbu funkcií, kde potrebujeme zistiť, či sa niektorý predmet nachádza v miestnosti alebo v zozname. To vieme okamžite využiť v implementácii príkazu `preskumaj`, kde aktuálne prehľadávame zoznam predmetov v miestnosti ručne. Úprava metódy `exec` bude vyzerať nasledovne:


```python
def exec(self, context):

```
