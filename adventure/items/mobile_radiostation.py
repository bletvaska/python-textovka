from helpers import get_item_by_name
from .features import MOVABLE, USABLE
from .item import Item


class MobileRadiostation(Item):
    name = 'prenosna radiostanica'
    description = 'Zdá sa, že je schopná prevádzky.'
    features = [MOVABLE, USABLE]
    used: bool = False

    def use(self, context):
        # check usage conditions
        battery = get_item_by_name('automobilova bateria', context.backpack + context.current_room.items)

        if battery is None:
            print('Bohužiaľ, nemáš žiadny zdroj elektriny.')

        elif self.used:
            print('Batéria je už tak slabá, že nič nie je počuť.')

        else:
            # use
            print('Podarilo sa ti spojiť s priateľmi v Káhire. Sľúbili, že po teba pošlú lietadlo.')
            print('Ale niečo za niečo... Chcú, aby si našiel faraónov platinový náhrdelník, ktorý Nemci hľadajú už '
                  'niekoľko mesiacov.')
            self.used = True

        return True
