# Resetovanie kontextu

Opätovne spustiť hru tým, že ju vypnete a zapnete znova, nie je veľmi dobrá používateľská skúsenosť. Upravíme teda kód tak, aby sme vedeli hru reštartovať priamo z jej prostredia samostatným príkazom `restart`.

Predtým, ako vytvoríme samotný príkaz `restart`, pridáme do kontextu metódu `.reset()`, ktorá kontext inicializuje. Inicializácia zabezpečí nasledovné:

* hráčov batoh bude prázdny
* zoznam príkazov bude prázdny
* zoznam miestností tvoriacich svet znovu nahráme zavolaním funkcie `get_world()`
* aktuálna miestnosť bude `lietadlo`
* stav hry zostane aj naďalej `PLAYING`


## Riešenie

```python
 def reset(self):
     self.game_state = PLAYING
     self.world = get_world()
     self.current_room = get_room_by_name('lietadlo', self.world)
     self.backpack = []
     self.history = []
```
