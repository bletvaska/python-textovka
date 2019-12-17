from commands import *


class Parser:
    def __init__(self):
        self.commands = [
            About(),
            Quit(),
            West(),
            East(),
            Down(),
            LookAround(),
            Examine(),
            Take(),
            Inventory(),
            Drop(),
            Use(),
            Save(),
            Load()
        ]
        self.commands.append(Commands(commands))

    def parse(self, line: str):
        for command in self.commands:
            if line.startswith(command._name) == True:
                command._params = line.split(command._name, 1)[1].strip()
                return command
