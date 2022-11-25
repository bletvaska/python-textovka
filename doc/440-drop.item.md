# Príkaz `poloz`

Vytvorte triedu `Drop`, ktorá bude reprezentovať príkaz `poloz`. Tento príkaz položí predmet z batohu do aktuálnej
miestnosti.

* názov príkazu: `poloz`
* opis príkazu: `vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti`

Príkaz musí spĺňať nasledovné podmienky:

   * Ak príkaz spustíme bez parametre (to znamená, že sme neuviedli, aký predmet chceme položiť), program vypíše na
     obrazovku správu `Neviem čo chceš položiť.`:

      ```
      > poloz
      Neviem čo chceš položiť.
      ```

   * Ak sa pokúsime položiť predmet, ktorý pri sebe nemáme, vypíšte na obrazovku správu `Taký predmet pri sebe nemáš.`:

     ```
     > poloz elektricka
     Taký predmet pri sebe nemáš.
     ```

   * Ak hráč úspešne položí predmet do miestnosti, vypíšte na obrazovku správu:

     ```
     > poloz bic
     Do miestnosti si položil bic.
     ```


## Riešenie

```python

```
