from context import Context


class Quit:
    def __init__(self):
        self._name = 'koniec'
        self._description = 'Ukončí aktuálnu hru.'

    def exec(self, context:Context):
        print('dakujem ze si si zahral, ale by si si to mohol aj rozmysliet, ci chces skoncit tuto mocnu hru.')
        context.game_state = 'QUIT'
