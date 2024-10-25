import states
from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from game_context import GameContext
from helpers import intro, outro, parse_line
from rooms.room import Room

intro()

# game initialization
context = GameContext(
    commands=[
        About(),
        Commands(),
        Inventory(),
        LookAround(),
        Quit()
    ]
)

context.current_room = Room(name='v lietadle',
            description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je '
                        'tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej '
                        'duše. (Celkom zaujímavá situácia, že áno?)',
            items=['bič', 'prázdne sedadlá'],
            exits=['dolu'])

# game loop
context.current_room.show()
while context.game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':
        continue

    command = parse_line(line, context.commands)
    if command is None:
        print('Taký príkaz nepoznám.')
    else:
        command.exec(context)

outro()
