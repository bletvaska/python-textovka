# Príkaz `koniec`

Pomocou tohto príkazu ukončíme hru. Aby však nedošlo k ukončeniu omylom, pred ukončením sa hráča najprv opýtame, či chce hru naozaj skončiť.

```python
class Quit(Command):
    name = 'koniec'
    description = 'ukončí rozohratú hru'

    def exec(self):
        choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
        if choice in ('ano', 'a', 'yes', 'y'):
            game_state = states.QUIT
```

Ak však tento príkaz spustíme a vyberieme si možnosť `ano`, hra sa žiaľ neukončí.
