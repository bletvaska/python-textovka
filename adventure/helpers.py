from commands import Command


def intro():
    """
    Shows the intro banner of the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('                   and his Great Python Adventure')
    print()


def outro():
    """
    Shows the outro screen of the game.
    """
    print('(c)2024 by mirek')
    print('See you soon.')


def parse_line(line: str, commands: list[Command]) -> Command | None:
    for command in commands:
        if line == command.name:
            return command

    # return None
