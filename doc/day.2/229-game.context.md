# Game Context

Aktuálne vkladáme pri volaní metódy `.exec()` nad jednotlivými príkazmi hry dva parametre: batoh a zoznam príkazov. Ak sa však nad tým zamyslíme, budeme mať tých parametrov stále viac a viac. A hádam nechceme skončiť ako knižnica _Pandas_, ktorá má funkcie s desiatkami parametrov... :-)

Miesto toho zabalíme všetky tieto parametre do jedného objektu, ktorý nazveme **herný kontext** alebo **kontext hry**. Bude sa jednať o triedu, ktorá bude mať len vlastnosti a žiadne metódy. Tieto vlastnosti budú potrebné na to, aby sme vedeli v každom momente hry povedať, čo sa deje a mali sme k dispozícii všetko potrebné.


## Lab: Trieda `GameContext`

Vytvorte triedu s názvom `GameContext` v module `game_context.py`. Táto trieda bude udržiavať herný kontext hry.

Trieda bude mať tieto členské premenné:

* `commands` - zoznam príkazov, ktoré vieme v hre použiť, a do ktorého rovno vložíme zoznam príkazov, ktorý máme zatiaľ vytvorený
* `game_state` - aktuálny stav hry, ktorý bude predvolene `PLAYING`
* `backpack` - hráčov batoh, ktorý bude predvolene prázdny


```python
class GameContext(BaseModel):
    backpack: list = []
    commands: list[Command] = [
      About(),
      Commands(),
      Quit()
    ],
    game_state: str = PLAYING
```

## Refaktoring

Po vytvorení inštancie je potrebné urobiť refaktoring a upraviť kód tak, aby používal kontext hry.
