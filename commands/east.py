class East:
    def __init__(self):
        self._name = 'vychod'
        self._description = 'Presunie sa do miestnosti na východ.'

    def exec(self, context):
        if 'east' in context.current_room._exits:
            context.current_room = context.current_room._exits['east']
            print(context.current_room)
        else:
            print('tam sa neda ist.')