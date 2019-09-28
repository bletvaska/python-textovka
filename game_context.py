# from items import Branch, GoldenIdol
from room import Room


class GameContext(object):
    def __init__(self):
        self.backpack = None
        self.world = {}
        self._rooms = []
        self.current_room = None
        self.state = 'playing'
        self.history = []

    def get_current_room(self) -> Room:
        for room in self._rooms:
            if room._name == self.current_room:
                return room

        # return self.world[self.current_room]

    def init_game(self):
        self._rooms = []

        room = Room('pred jaskynou',
                    'Stojis pred vchodom do tajomnej jaskyne. Jaskyna nevesti nic dobre.') \
            .set_exit('vychod', 'v jaskyni')
        self._rooms.append(room)

        room = Room('v jaskyni',
                    'Stojis v temnej jaskyni. Uz aj tak mizernu viditelnost znizuju este pavuciny, ktorych je tu teda riadna kopa.') \
            .set_exit('zapad', 'pred jaskynou') \
            .set_exit('vychod', 'nad priepastou')
        self._rooms.append(room)

        room = Room('nad priepastou',
                    'Okrem pavucin a nahodne skakjucich tarantul tu nie je nic zaujimave. Pokial za zaujimave nepokladas tu priepast, ktora zabera vacsinu vyhladu v tejto miestnosti.') \
            .set_exit('zapad', 'v jaskyni') \
            .set_exit('dolu', 'priepast')
        # .add_item(Branch())
        self._rooms.append(room)

        room = Room('priepast',
                    'Dno priepaste posiate kostrami rozlicneho vzrastu. Zrejme sa jedna o nahodnych turistov, ktori svoj vylet nestihli dokoncit. Alebo len preskocit.')
        self._rooms.append(room)

        room = Room('chram',
                    'Rozlahla miestnost, v strede ktorej sa nachadza oltar, na ktorom je este stale umiestneny ciel tvojej cesty: Golden Idol.') \
            .set_exit('zapad', 'nad priepastou')
        # .add_item(GoldenIdol())
        self._rooms.append(room)

        self.current_room = 'pred jaskynou'
