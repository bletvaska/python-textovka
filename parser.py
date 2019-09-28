from exceptions import UnknownCommandException


class Parser(object):
    def __init__(self, commands):
        self._commands = commands

    def parse(self, line:str):
        line = line.strip().lower()

        for command in self._commands:
            for alias in command.aliases:
                if line.startswith(alias):
                    params = line[len(alias):].strip()
                    command.params = params
                    return command
        else:
            raise UnknownCommandException(f'Neznámy príkaz: {line}')
