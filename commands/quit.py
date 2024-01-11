import states
from commands.command import Command


class Quit(Command):
    """
    Quits the game.
    """
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def exec(self, context):
        choice = input('Naozaj chceš skončiť? (a/n) ').lower().strip()

        if choice in ('a', 'y', 'ano', 'yes'):
            print('Ďakujem, že si si zahral túto úžasnú (ukradnutú) hru.')
            context.game_state = states.QUIT
