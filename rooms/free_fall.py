import states
from items.empty_seats import EmptySeats
from items.whip import Whip
from . import directions
from .room import Room


class FreeFall(Room):
    name = 'voľný pád'
    description = 'Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a nevšímaj si zem, ktorá sa rapídne približuje. Mimochodom, v diaľke na [bold yellow]juhu[/bold yellow] je vidieť nejaký vojenský tábor.'
    counter = 0

    def act(self, context):
        self.counter = self.counter + 1

        if self.counter == 2:
            print('Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie ako skok hlboký.')
            context.game_state = states.STATE_DEATH
