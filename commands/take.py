import states
from commands.command import Command
from items.features import EXAMINABLE, MOVABLE
from rooms.room import Room


class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        if self.param == '':
            print('Neviem, čo chceš zobrať.')
        else:
            for item in context.current_room.items:
                if item.name == self.param:
                    # is item movable?
                    if MOVABLE in item.features:
                        # odstranim z miestnosti
                        context.current_room.items.remove(item)
                        # vlozim do batohu
                        context.backpack.append(item)
                        # render
                        print(f'Do batohu si vložil predmet {item.name}.')
                    else:
                        print('Tento predmet sa nedá zobrať.')
                    return

            print('Taký predmet tu nikde nevidím.')
