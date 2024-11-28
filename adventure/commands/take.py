from rich import print

from items.features import MOVABLE
from .command import Command


class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        # if not item was entered
        if self.param == '':
            print('Neviem, čo chceš zobrať.')
            return

        for item in context.current_room.items:
            if self.param == item.name:
                if MOVABLE not in item.features:
                    print('Tento predmet sa nedá zobrať.')
                    return

                if len(context.backpack) >= 5:
                    print('Batoh je plný.')
                    return

                context.backpack.append(item)
                context.current_room.items.remove(item)
                print(f'Do batohu si vložil predmet [bold magenta]{self.param}[/bold magenta].')
                return

        print('Taký predmet tu nikde nevidím.')
