import json

from .command import Command


class Load(Command):
    name: str = 'nahraj'
    description: str = 'načíta uloženú pozíciu hry zo súboru'

    def exec(self, context, filename):
        if filename == '':
            print('Neviem, z akého súboru chceš načítať svoju uloženú pozíciu.')
            return

        with open(filename, 'r') as file:
            history = json.load(file)

        # new_context = GameContext()
        # new_context.current_room = get_room_by_name('lietadlo', context.world)
        #
        # for line in history:
        #     cmd, param = parse_line(line, new_context.commands)
        #     cmd.exec(new_context, param)

        for line in history:
            print(line)

        print('Tvoja pozícia bola úspešne načítaná.')

