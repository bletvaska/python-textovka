from items.item import Item
# from items.mixins import Movable
from items import mixins


class Whip(Item, mixins.Movable, mixins.Usable):
    def __init__(self):
        super().__init__('bic',
                         'Ta mocny bic na krotenie levov, ktory si si zohnal ako mlady chalanisko v tretej casti serie.')

    def use(self, context):
        if context.current_room != 'nad priepastou':
            print('Svihol si bičíkom vo vzduchu. Ale švihá, pomyslel si si. Ako za mladých čias.')
            return

        room = context.world[context.current_room]
        # pridanie prechodu z miestnosti na vychod
        room['exits']['vychod'] = 'chram'

        # vyhodenie bica z miestnosti alebo z batohu
        for item in context.backpack:
            if item._name == 'bic':
                context.backpack.remove(item)
                break
        else:
            for item in room['items']:
                if item._name == 'bic':
                    room['items'].remove(item)
                    break

        print(
            'Rozohnal si sa, vzduchom to zasvišťalo a tvoj bič sa zachytil o visiaci konár v hornej časti jaskyne. Prehupnúť sa na druhú stranu už nebude žiadny problém.')
