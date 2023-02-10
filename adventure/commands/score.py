from rich import print

from .command import Command


class Score(Command):
    name = 'skore'
    description = 'zobrazí dosiahnuté skóre hry.'

    def exec(self, context) -> None:
        print(f'Zatiaľ si zvládol [yellow]{context.score}%[/yellow] hry.')
