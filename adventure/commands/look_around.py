from commands.command import Command


class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'rozhliadne sa v aktualnej miestnosti'

    def exec(self, context):
        context.current_room.show()
