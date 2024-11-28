from .command import Command


class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        # if not item was entered
        if self.param == '':
            print('Neviem, čo chceš zobrať.')
            return

        print(f'pokusam sa zobrat predmet {self.param}.')
