from commands.command import Command


class Load(Command):
    def __init__(self):
        super().__init__('nahraj', 'Načíta stav hry zo súboru.')

    def exec(self, context):
        # ak nebol zadany prikaz s nazvom suboru
        if len(self._params) == 0:
            print('Chýba názov súboru.')
            return

        with open(self._params) as f:
            context.init_game()
            for line in f.readlines():
                print(line)



        print('ta subor bol uspesne nacitany.')
