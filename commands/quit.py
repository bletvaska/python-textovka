from commands.command import Command


class Quit(Command):
    def __init__(self):
        super().__init__('koniec', 'Ukončí aktuálnu hru.')

    def exec(self, context):
        print('dakujem ze si si zahral, ale by si si to mohol aj rozmysliet, ci chces skoncit tuto mocnu hru.')
        context.game_state = 'QUIT'
