from rich import print

from .command import Command


class Score(Command):
    name = 'skore'
    description = 'zobrazí dosiahnuté skóre'

    def exec(self, context):
        print(f'Zatiaľ si zvládol [yellow]{context.score}%[/yellow] hry.')
