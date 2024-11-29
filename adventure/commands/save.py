import json

from rich import print

from .command import Command


class Save(Command):
    name: str = 'uloz'
    description: str = 'uloží rozohratú hru'

    def exec(self, context):
        path = self.param

        if path == '':
            print('[bold red]Súbor nebol zadaný.[/bold red]')
            return

        with open(path, 'w') as file:
            json.dump(context.history, file)
            print('[bold green]Stav hry bol úspešne uložený.[/bold green]')
