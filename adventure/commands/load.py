import json

from .command import Command


class Load(Command):
    name: str = 'nahraj'
    description: str = 'nahrá uloženú pozíciu hry zo súboru'

    def exec(self, context, filename):
        if filename == '':
            print('Neviem, z akého súboru chceš nahrať svoju uloženú pozíciu.')
            return

        with open(filename, 'r') as file:
            history = json.load(file)

        print('Tvoja pozícia bola úspešne nahraná.')

        for line in history:
            print(line)
