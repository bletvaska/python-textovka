from game_context import GameContext
from .command import Command


class ExamineItem(Command):
    def __init__(self):
        super().__init__("preskumaj", "Preskúma zvolený predmet.")

    def exec(self, context:GameContext):
        name = self.params

        # search in backpack
        if name in context.backpack:
            print(context.backpack[name].description)
            return

        room = context.get_current_room()
        items = room['items']

        for item in items:
            if item.name == self.params:
                print(item.description)
                return

        print('Taký predmet tu nikde nevidím.')