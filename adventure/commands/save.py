import json

from .command import Command


class Save(Command):
    name: str = 'uloz'
    description: str = 'uloží aktuálny stav hry do súboru'

    def exec(self, context, filename):
        if filename == '':
            print('Neviem, do akého súboru chceš ulož svoju pozíciu.')
            return

        with open(filename, 'w') as file:
            json.dump(context.history, file)
            print('Pozícia bola úspešne uložená.')

        # return None
