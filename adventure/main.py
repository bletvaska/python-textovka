import states
from game_context import GameContext
from helpers import intro, outro, parse_line
from items.empty_seats import EmptySeats
from items.whip import Whip
from rooms.room import Room

intro()

# game initialization
context = GameContext()

context.current_room = Room(name='v lietadle',
                            description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je '
                                        'tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej '
                                        'duše. (Celkom zaujímavá situácia, že áno?)',
                            items=[
                                Whip(),
                                EmptySeats()
                            ],
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
