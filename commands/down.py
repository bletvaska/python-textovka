class Down:
    def __init__(self):
        self._name = 'dolu'
        self._description = 'Presunie sa do miestnosti nachádzajúcej sa dolu od aktuálnej.'

    def exec(self, context):
        if 'down' in context.current_room._exits:
            context.current_room = context.current_room._exits['down']
            print(context.current_room)
        else:
            print('tam sa neda ist.')