from game_context import GameContext
from items.mixins import UsableMixin
from .command import Command


class UseItem(Command):
    def __init__(self):
        super().__init__("pouzi", "Použije zvolený predmet.")
        self.aliases += ['use']

    def exec(self, context:GameContext):
        room = context.get_current_room()
        items = room['items'] + context.backpack

        for item in items:
            if item.name == self.params:
                if not isinstance(item, UsableMixin):
                    print('Tento predmet sa nedá použiť')
                    return

                context.history.append(f'{self.name} {item.name}')
                item.use(context)

        print('Taký predmet tu nikde nevidím.')