from .command import Command


class LookAround(Command):
    # fields, attributes
    name: str = 'rozhliadni sa'
    description: str = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, context):
        context.current_room.show()
