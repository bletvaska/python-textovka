# Rozpoznávanie príkazov s parametrom

Príkazy, ktoré naša hra obsahuje, sú zatiaľ veľmi jednoduché, pretože neobsahujú žiadny parameter. V hre však budeme mať aj príkazy, ktoré budú pracovať s parametrom, ako napríklad:

* `preskumaj predmet`
* `vezmi predmet`
* `pouzi predmet`
* a pod.

Náš jednoduchý parser momentálne dokáže rozpoznávať len príkazy, ktoré parameter nemajú. Aby sme mohli pracovať s príkazmi, ktoré
majú parameter, musíme ho upraviť. 

### Rozpoznanie príkazu s parametrom

Momentálne na rozpoznanie príkazu používame operátor `==`. Očakávame totiž, že to, čo hráč zadá na štandardný vstup, bude celý názov príkazu. To však platí iba vtedy, ak sa jedná o príkazy bez parametrov. Ak totiž hráč na vstupe napíše:

```
> preskumaj hrncek
```

tak náš parser nebude hľadať príkaz s menom `preskumaj`, ale bude hľadať príkaz s menom `preskumaj hrncek`.


Pri rozpoznávaní príkazov teda nemôžeme očakávať jeho presné znenie, ale budeme čakať, že vstup od používateľa sa bude
začínať názvom príkazu. To vieme overiť volaním metódy `.startswith()` (alebo aj metódy `.index()`) nad reťazcom so
vstupom od používateľa:

```python
>>> 'preskumaj bic'.startswith('preskumaj')
True
>>> 'preskumaj bic'.startswith('o hre')
False
```

Aktualizujeme teda parser nasledovne:

```python
def parse_line(line: str, commands: list[Command]) -> Command | None:
    for command in commands:
        if line.startswith(command.name):
            return command
    return None
```

Všetko funguje tak, ako doteraz a ako bonus parser teraz rozpozná aj príkaz `preskumaj` s parametrom.

## Parameter príkazu

Potrebujeme však ešte získať parameter, ktorým je názov predmetu, a ktorý je zadaný za príkazom.
