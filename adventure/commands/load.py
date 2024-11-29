import json

from rich import print

from helpers import parse_line
from states import LOADING, PLAYING
from .command import Command


class Load(Command):
    name: str = 'nahraj'
    description: str = 'načíta uloženú hru'

    def exec(self, context):
        path = self.param

        if path == '':
            print('[bold red]Súbor na načítanie nebol zadaný.[/bold red]')
            return

        with open(path, 'r') as file:
            history = json.load(file)

            context.reset()
            context.game_state = LOADING

            for line in history:
                cmd = parse_line(line, context.commands)
                cmd.exec(context)

            context.game_state = PLAYING

        print('[bold green]Pozícia bola úspešne nahraná.[/bold green]')
