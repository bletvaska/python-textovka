from rich import print

from helpers import get_item_by_name
from .command import Command


class Drop(Command):
    name = 'poloz'
    description = 'položí zvolený predmet'

    def exec(self, context):
        # when no param was given
        # len(self.param) == 0
        if self.param == '':
            print('Neviem, aký predmet chceš položiť.')

        else:

            # search for item in backpack
            item = get_item_by_name(self.param, context.backpack)

            if item == None:
                print('Taký predmet pri sebe nemáš.')
            else:
                # drop item in current room
                context.backpack.remove(item)
                context.current_room.items.append(item)

                # render
                print(f'V miestnosti si položil predmet [magenta bold]{item.name}[/magenta bold].')



            # for item in context.backpack:
            #     if item.name == self.param:
            #         # drop item in current room
            #         context.backpack.remove(item)
            #         context.current_room.items.append(item)
            #
            #         # render
            #         print(f'V miestnosti si položil predmet [magenta bold]{item.name}[/magenta bold].')
            #
            #         break
            # else:
            #     print('Taký predmet pri sebe nemáš.')

