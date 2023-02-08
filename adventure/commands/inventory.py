from .command import Command


class Inventory(Command):
    name = 'inventar'
    description = 'zobrazí obsah hráčovho batohu'

    def exec(self, context) -> str:
        if len(context.backpack) == 0:
            print('Batoh je prázdny')

        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'  {item.name}')
