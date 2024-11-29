# História príkazov

Hru rozšírime o možnosť ukladať aktuálnu pozíciu. Možností, ako to spraviť, je samozrejme viacero. My ju implementujeme tak, že aktuálnu pozíciu budeme reprezentovať príkazmi, ktoré je potrebné zadať od spustenia hry až po moment jej uloženia.

Za týmto účelom potrebujeme rozšíriť kontext hry, do ktorého pridáme novú členskú premennú `history`, ktorá bude reprezentovať zoznam všetkých príkazov:

```python
history: list[str] = []
```

Následne je potrebné do histórie pridať každý jeden príkaz, ktorý sa podieľa na úspešnom riešení hry. A pridať ho treba v momente, keď je jasné, že sa naozaj vykoná (napr. je zbytočné pridávať príkazy, ktoré vyžadujú parameter, bez parametra).
