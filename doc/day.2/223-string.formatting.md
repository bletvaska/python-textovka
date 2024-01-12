# Formátovanie reťazcov

krajsie vypisovat by sme to chceli

```python
f'{}'
```


## Upravenie vypisu inventara

Zoznam veci chceme vypisovat takto:

```
V batohu máš:
* bic
```

## Riešenie

```python
    def exec(self, backpack) -> str:
        if backpack == []:
            print("Batoh je prázdny.")
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f'* {item}')
```
