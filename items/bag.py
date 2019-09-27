from game_context import GameContext
from .sand_pile import SandPile
from items.item import Item
from items.mixins import Movable, Usable


class Bag(Item, Movable, Usable):
    def __init__(self):
        super().__init__('vrecko', 'Prázdne vrecko.')
        self.is_full = False

    def use(self, context: GameContext):
        if not self.is_full:
            room = context.get_current_room()

            for item in room['items']:
                if isinstance(item, SandPile):
                    # trapna zmena stavu
                    self._name = 'vrecko piesku'
                    self._description = 'Vrecko plné piesku.'

                    print(
                        'Svoje mocné dlane si ponoril do chladného a drsného piesku, ktorým si naplnil doteraz prázdne vrecko. Až po okraj.')
                    self.is_full = True
                    break
            else:
                print(
                    'Poobzeral si si vrecko a uistil si sa, že v ňom nie je žiadna diera. Alebo si chcel od vrecka viac?')

        else:
            print('Ta už sa do neho viac nezmestí. Už je dosť plné. Teda tak akurát.')
