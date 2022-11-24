from dataclasses import dataclass

from .command import Command


@dataclass
class Help(Command):
    name: str = 'pomoc'
    description: str = 'zobrazí pomocníka ku zvolenému príkazu'

    def exec(self, context):
        for command in context.commands:
            if command.name == self.param:
                print(f'{command.name} - {command.description}')
                break
        else:
            print('Zatiaľ sa ti darí dosť dobre.')
