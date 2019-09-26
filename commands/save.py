from game_context import GameContext
from .command import Command


class Save(Command):
    def __init__(self):
        super().__init__('uloz', 'Ulozi aktualny stav na disk.')

    def exec(self, context: GameContext):
        if len(self.params) == 0:
            print('Chýba názov súboru.')
        else:
            with open(self.params, 'w') as file:
                for command in context.history:
                    file.write(f'{command}\n')

            print(f'Hra bola úspešne uložená do súboru {self.params}')
