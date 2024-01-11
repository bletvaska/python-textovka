import states
from commands.command import Command
from items.features import EXAMINABLE
from rooms.room import Room


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        if self.param == '':
            print('Neviem, čo chceš preskúmať.')
        else:
            for item in context.current_room.items:
                if item.name == self.param:
                    print(item.description)

                    # is item examinable?
                    if EXAMINABLE in item.features:
                        input('Skúmam...')
                        item.examine(context)

                    return

            print('Taký predmet tu nikde nevidím.')
