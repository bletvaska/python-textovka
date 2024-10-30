from rich import print

from items.features import MOVABLE
from .command import Command


class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z aktuálnej miestnosti a vloží ho do batohu'

    def exec(self, context, param):
        if param == '':
            print('Neviem, čo chceš zobrať.')
            return

        for item in context.current_room.items:
            if param == item.name:

                if MOVABLE in item.features:
                    context.current_room.items.remove(item)
                    context.backpack.append(item)
                    print(f'Do batohu si vložil predmet [bold magenta]{item.name}[/bold magenta].')
                else:
                    print('Tento predmet sa nedá zobrať.')

                break
        else:
            print('Taký predmet tu nikde nevidím.')
