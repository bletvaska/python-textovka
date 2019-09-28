from commands.command import Command
from exceptions import ItemNotFoundException
from game_context import GameContext


class DropItem(Command):
    def __init__(self):
        super().__init__("poloz", "Položí predmet v miestnosti.")
        self.aliases += ['drop']

    def exec(self, context: GameContext):
        try:
            item = context.backpack.remove_item(self.params)
            room = context.get_current_room()
            room['items'].append(item)
            print(f'{item.name} si vyložil z batohu.')
            context.history.append(f'{self.name} {self.params}')
        except ItemNotFoundException:
            print('Taký predmet u seba nemáš.')
