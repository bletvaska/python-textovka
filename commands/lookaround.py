from commands.command import Command


class LookAround(Command):
    def __init__(self):
        super().__init__('rozhliadni sa', 'Ta kukaj het, čo je v miestnosti.')

    def exec(self, context):
        print(context.current_room)