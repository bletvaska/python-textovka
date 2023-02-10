import json

from .command import Command


class Save(Command):
    name = 'uloz'
    description = 'uloží aktuálny stav hry do súboru'

    def exec(self, context):
        # if no filename was entered
        filename = self.param
        if filename == '':
            print("Nezadal si názov súboru.")
            return

        with open(filename, 'w') as file:
            json.dump(context.dict(), file, indent=4, ensure_ascii=False)

        print('Pozícia bola úspešne uložená.')
