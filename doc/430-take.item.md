# Prikaz `vezmi predmet`

trieda: Take
nazov: vezmi
opis: vezme predmet z miestnosti a vloží ho do batohu

Vytvorte prikaz `vezmi`, pomocou ktoreho budete vedieť vziať predmet z miestnosti a vložiť ho do batohu.

   * Samozrejme musíme sa na príkaz `VEZMI` pripraviť. Ak príkaz spustíme bez parametre (to znamená, že sme neuviedli,
   aký predmet chceme zobrať), program vypíše na obrazovku správu `Neviem, čo chceš zobrať.`. Napríklad:

   ```
    $ VEZMI
    Neviem, čo chceš zobrať.
   ```

   * Ak chceme vziať predmet z miestnosti, musí sa nachádzať v zozname predmetov, ktoré sa v miestnosti nachádzajú.
     Ak zasa hráč napíše názov predmetu, ktorý sa v miestnosti nenachádza, vypíšte na obrazovku text `Taký predmet tu nikde nevidím.`

   ```
    $ VEZMI elektricka
    Taký predmet tu nikde nevidím.
   ```

   Takže predmet je možné z miestnosti vziať len vtedy, ak sa nachádza v zozname predmetov danej miestnosti. V tom momente je potrebné predmet odstrániť z tohto zoznamu a vložiť ho do inventára.
