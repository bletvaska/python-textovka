#!/usr/bin/env python3

def go_west(context):
    if 'west' in context.current_room._exits:
        context.current_room = context.current_room._exits['west']
        print(context.current_room)
    else:
        print('tam sa neda ist.')


def go_east(context):
    if 'east' in context.current_room._exits:
        context.current_room = context.current_room._exits['east']
        print(context.current_room)
    else:
        print('tam sa neda ist.')


def go_down(context):
    if 'down' in context.current_room._exits:
        context.current_room = context.current_room._exits['down']
        print(context.current_room)
    else:
        print('tam sa neda ist.')

def commands():
    print('Zoznam prikazov:')
    print('\tkoniec - ukonci tuto mocnu hru')
    print('\to autorovi - zobrazi info o autorovi')
    print('\tprikazy - zobrazi zoznam prikazov')

def about():
    print(
        'ta to je iny sumny mladenec toten autor. by si ho mohol podporit mocnym fsimnym na ucet SK1234567890. ale fakt mocnym.')
    print('to je asi fsetko, co by si o nom mohol vediet. verejne.')

def quit(context):
    print('dakujem ze si si zahral, ale by si si to mohol aj rozmysliet, ci chces skoncit tuto mocnu hru.')
    context.game_state = 'QUIT'


class Context:
    def __init__(self):
        self.game_state = 'PLAYING'
        self.world = {}

        self.world['kabina'] = Room('kabina',
                               'Vošiel si do kabíny pilotov, ktorá sa skrývala za voľne zatiahnutým závesom. Aj tu je kľud. Nikto tu nie je. Kniple sa voľne pohupujú a ručičky na budíkoch sa voľne otáčajú.')

        self.world['vo vzduchu'] = Room('vo vzduchu',
                                   'Voľne sa vznášaš v priestore a vychutnávaš si ostrý vzduch. Tvoju pozornosť rozptyľujú len zväčšujúce sa bodky na zemi. Krásne je dnes vonku.')

        self.world['prva trieda'] = Room('prva trieda',
                                    'Prvá trieda. Sliepky a iné živočíchy tu cestujú s tebou tiež. Na sedadlách sa nachádzajú klietky a iný spotrebný materiál.')

        self.world['batozinovy priestor'] = Room('batozinovy priestor',
                                            'Veľa priestoru pre padáky. Škoda, že tu žiadny nevidno.')

        self.world['kabina'].add_exit('east', self.world['prva trieda'])
        self.world['prva trieda'].add_exit('east', self.world['batozinovy priestor'])
        self.world['prva trieda'].add_exit('west', self.world['kabina'])
        self.world['prva trieda'].add_exit('down', self.world['vo vzduchu'])
        self.world['batozinovy priestor'].add_exit('west', self.world['prva trieda'])

        self.current_room = self.world['prva trieda']


class Room:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._exits = {}

    def add_exit(self, name, room):
        if isinstance(room, Room):
            self._exits[name] = room
        else:
            raise TypeError('Not a Room object.')


    def __str__(self) -> str:
        return self._description

    def __repr__(self):
        return f'repr: "{self._name}". {self._description}'


context = Context()


print('Indiana Jones and the Plane Escape')

print(
    'Ta si sa zobudil v prvej triede lietadla spoločnosti Lao Che. To ticho ti až bilo do uší. Lietadlo vraj nikto nešoféruje a aj motory sú už vypnuté.')

print(context.current_room)

while context.game_state == 'PLAYING':
    line = input('> ').strip().lower()

    if line in ('koniec', 'quit', 'k', 'q'):
        quit(context)

    elif line in ('o autorovi', 'o mne', 'info'):
        about()

    elif line in ('prikazy', 'prikaz', 'commands'):
        commands()

    elif line in ('zapad', 'z', 'west', 'w'):
        go_west(context)

    elif line in ('vychod', 'v', 'east', 'e'):
        go_east(context)

    elif line in ('dolu', 'down'):
        go_down(context)

    else:
        print('taky prikaz nepoznam.')
