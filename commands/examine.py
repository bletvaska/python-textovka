from items.features import EXAMINABLE
from .command import Command


class Examine(Command):
    name = 'preskumaj'
    description = 'preskúma zvolený predmet'

    def exec(self, context):
        # when no param was given
        # len(self.param) == 0
        if self.param == '':
            print('Neviem, aký predmet chceš preskúmať.')

        else:

            for item in context.current_room.items + context.backpack:
                if item.name == self.param:
                    print(item.description)

                    # check if item is examinable
                    if EXAMINABLE in item.features:
                        item.examine(context)
                        
                    break
            else:
                print('Taký predmet tu nikde nevidím.')

