from commands.command import Command


def intro():
    """
    Shows the intro screen of the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('                   and his Greatest Python Adventure')
    print()


def outro():
    """
    Shows the outro (credits) screen of the game. Also asks for MONEY.
    """
    print('(c)2024 ukradol mirek')
    print('Dakujem ze si si zahral. Nabuduce zaplat.')


def parse_line(line: str, commands: list[Command]) -> Command | None:
    for command in commands:
        if line == command.name:
            return command

    return None  # default
