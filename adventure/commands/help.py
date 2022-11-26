from .command import Command


class Help(Command):
    name = 'pomoc'
    description = 'zobrazí pomocníka ku zvolenému príkazu'

    def exec(self, context):
        for command in context.commands:
            if command.name == self.param:
                print(f'{command.name} - {command.description}')
                break
        else:
            print('Zatiaľ sa ti darí dosť dobre.')
