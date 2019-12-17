from commands.command import Command


class Down(Command):
    def __init__(self):
        super().__init__('dolu', 'Presunie sa do miestnosti nachádzajúcej sa dolu od aktuálnej.')

    def exec(self, context):
        if 'down' in context.current_room._exits:
            context.current_room = context.current_room._exits['down']
            print(context.current_room)

            # ulozi prikaz do historie
            self.save_to_history(context)
        else:
            print('tam sa neda ist.')
