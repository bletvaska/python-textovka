from commands.command import Command
from game_context import GameContext


class DropItem(Command):
    def __init__(self):
        super().__init__("poloz", "Položí predmet v miestnosti.")

    def exec(self, context:GameContext):
        room = context.get_current_room()
        for item in context.backpack:
            if item.name == self.params:
                room['items'].append(item)
                context.backpack.remove(item)
                print(f'{item.name} si vyložil z batohu.')
                context.history.append(f'{self.name} {self.params}')
                break
        else:
            print('Taký predmet u seba nemáš.')