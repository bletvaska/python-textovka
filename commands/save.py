from commands.command import Command


class Save(Command):
    def __init__(self):
        super().__init__('uloz', 'Uloží stav hry do súboru.')

    def exec(self, context):
        # ak nebol zadany prikaz s nazvom suboru
        if len(self._params) == 0:
            print('Chýba názov súboru.')
            return

        for cmd in context.history:
            print(cmd)