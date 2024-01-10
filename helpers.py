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
    print("Indiana Jones and his Greatest Python Adventure".center(70))


def outro():
    """
    Shows the outro screen of the game.
    """
    print('(c)2024 mirek')
    print('See you soon')


def parse_line(line: str, commands: list[Command]) -> Command | None:
    """
    Parse a command from user's input and return command if found.
    """
    for command in commands:
        if line.startswith(command.name):
            command.param = line.split(command.name, maxsplit=1)[1].lstrip()
            return command

    return None
