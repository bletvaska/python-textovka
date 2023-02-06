from pyfiglet import Figlet


def intro():
    """
    Shows the intro screen of the game.
    """
    figlet = Figlet()
    banner = figlet.renderText('Indiana Jones')
    print(banner)
    print('                        and his Great Python Adventure')
    print()


def outro():
    """
    Shows the outro screen of the game.
    """
    print('(c)2023 by mirek')
    print('Thanks for playing')
