from rich import print

from game_context import GameContext
from helpers import get_room_by_name
from items.features import USABLE, MOVABLE
from items.item import Item


class Parachute(Item):
    name: str = 'padak'
    description: str = 'obyčajný padák. Made in U.S.A. 1933'
    features: list[int] = [MOVABLE, USABLE]

    def use(self, context: GameContext):
        # sme v spravnej miestnosti?
        if context.current_room.name != 'vo vzduchu':
            print('Podľa teba som zrejme blbec, ale naozaj nechápem, na čo by to v tejto chvíli bolo dobré.')
            return

        # presun sa do miestnosti pust
        context.current_room = get_room_by_name('púšť', context.world)

        # render
        print('[bold green]Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...[/bold green]')
        context.current_room.show()
