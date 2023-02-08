from .command import Command


class Inventory(Command):
    name = 'inventar'
    description = 'zobrazí obsah hráčovho batohu'

    def exec(self, context) -> str:
        # check if backpack is empty
        if len(context.backpack) == 0:  # context.backpack == []
            print('Batoh je prázdny')
            return

        # print content of backpack
        print('V batohu máš:')
        for item in context.backpack:
            print(f'  {item.name}')
