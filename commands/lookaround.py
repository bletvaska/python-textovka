class LookAround:
    def __init__(self):
        self._name = 'rozhliadni sa'
        self._description = 'Ta kukaj het, čo je v miestnosti.'

    def exec(self, context):
        print(context.current_room)