"""
Game Context Module
"""
from backpack import Backpack
from items import Whip, Revolver, Fedora, RubberBoat, Seats, Key, DoorToLuggage
from room import Room, DeadRoom


def add(a, b):
    """
    spocitaj daco

    >>> add(10, 20)
    30
    >>> add(0, 0)
    10
    """
    return a+b


class Context:
    """
    Game context
    """
    def __init__(self):
        self.game_state = 'PLAYING'
        self.world = {}
        self.backpack = Backpack()
        self.backpack += Key()

        self.world['kabina'] = Room('kabina',
                               'Vošiel si do kabíny pilotov, ktorá sa skrývala za voľne zatiahnutým závesom. Aj tu je kľud. Nikto tu nie je. Kniple sa voľne pohupujú a ručičky na budíkoch sa voľne otáčajú.')

        self.world['vo vzduchu'] = Room('vo vzduchu',
                                   'Voľne sa vznášaš v priestore a vychutnávaš si ostrý vzduch. Tvoju pozornosť rozptyľujú len zväčšujúce sa bodky na zemi. Krásne je dnes vonku.')

        self.world['prva trieda'] = Room('prva trieda',
                                    'Prvá trieda. Sliepky a iné živočíchy tu cestujú s tebou tiež. Na sedadlách sa nachádzajú klietky a iný spotrebný materiál.')
        self.world['prva trieda']._items.append(Whip())
        self.world['prva trieda']._items.append(Revolver())
        self.world['prva trieda']._items.append(Fedora())
        self.world['prva trieda']._items.append(Seats())
        self.world['prva trieda']._items.append(DoorToLuggage())

        self.world['batozinovy priestor'] = Room('batozinovy priestor',
                                            'Veľa priestoru pre padáky. Škoda, že tu žiadny nevidno.')
        self.world['batozinovy priestor']._items.append(RubberBoat())

        self.world['zem'] = DeadRoom('zem', 'Ta si bezpečne dorazil na zem. Len škoda, že bez padáku. Technické služby budú mať zasa o robotu navyše. S tebou.')

        self.world['kabina'].add_exit('east', self.world['prva trieda'])
        # self.world['prva trieda'].add_exit('east', self.world['batozinovy priestor'])
        self.world['prva trieda'].add_exit('west', self.world['kabina'])
        self.world['prva trieda'].add_exit('down', self.world['vo vzduchu'])
        self.world['batozinovy priestor'].add_exit('west', self.world['prva trieda'])
        self.world['vo vzduchu'].add_exit('down', self.world['zem'])

        self.current_room = self.world['prva trieda']
