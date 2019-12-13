from commands.command import Command


class Inventory(Command):
    def __init__(self):
        super().__init__('inventar', 'vypíše obsah batohu.')

    def exec(self, context):
        if len(context.backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('Nesieš so sebou:')
            for item in context.backpack:
                print(f'\t{item._name}')