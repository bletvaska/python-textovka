from .command import Command


class Save(Command):
    name = 'uloz'
    description = 'uloží aktuálny stav hry do súboru'

    def exec(self, context):
        print('História príkazov:')
        for line in context.history:
            print(f'* {line}')
