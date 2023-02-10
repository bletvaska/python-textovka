import json

from .command import Command


class Load(Command):
    name = 'nacitaj'
    description = 'načíta stav hry zo súboru'

    def exec(self, context) -> None:
        # if no filename was entered
        filename = self.param
        if filename == '':
            print("Nezadal si názov súboru.")
            return

        with open(filename, 'r') as file:
            new_context = json.load(file)
            print(new_context)

        print('Pozícia bola úspešne načítaná.')
