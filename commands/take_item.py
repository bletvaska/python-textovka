from game_context import GameContext
from items.mixins import MovableMixin
from .command import Command


class TakeItem(Command):
    def __init__(self):
        super().__init__("vezmi", "Vezme predmet z miestnosti.")

    def exec(self, context:GameContext):
        room = context.get_current_room()
        for item in room['items']:
            if item.name == self.params:
                if not isinstance(item, MovableMixin):
                    print('Tento predmet sa nedá vziať.')
                elif len(context.backpack) >= 1:
                    print('Batoh je plný.')
                else:
                    context.backpack.add_item(item)
                    room['items'].remove(item)
                    print(f'{item.name} si vložil do batohu.')
                    context.history.append('f{self.name} {item.name}')

                break  # return
        else:
            print('Taký predmet tu nikde nevidím.')