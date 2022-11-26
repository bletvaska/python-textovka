from .command import Command


class Inventory(Command):
    # fields
    name = 'inventar'
    description = 'zobrazí obsah hráčovho batohu'

    # methods
    def exec(self, context):
        if len(context.backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'* {item.name}')
