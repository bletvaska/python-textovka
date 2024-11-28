from .command import Command


class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        print(f'pokusam sa zobrat predmet {self.param}.')
