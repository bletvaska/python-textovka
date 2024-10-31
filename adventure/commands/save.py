import json

from .command import Command


class Save(Command):
    name: str = 'uloz'
    description: str = 'uloží aktuálny stav hry do súboru'

    def exec(self, context, filename):
        if filename == '':
            print('Neviem, do akého súboru chceš ulož svoju pozíciu.')
            return

        file = open(filename, 'w')
        json.dump(context.history, file)
        file.close()

        print('Pozícia bola úspešne uložená.')
