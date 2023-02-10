from rich import print

from helpers import get_item_by_type
from . import CarBattery
from .features import MOVABLE, USABLE
from .item import Item


class MobileRadiostation(Item):
    name = 'prenosnu radiostanicu'
    description = 'Zdá sa, že je schopná prevádzky.'
    features = [MOVABLE, USABLE]
    used: bool = False

    def on_use(self, context):
        # check usage conditions
        battery = get_item_by_type(CarBattery, context.backpack)

        if battery is None:
            print('Bohužiaľ, nemáš žiadny zdroj elektriny.')

        elif self.used is True:
            print('Batéria je už tak slabá, že nič nie je počuť.')

        else:
            # use
            print('Podarilo sa ti spojiť s priateľmi v Káhire. Sľúbili, že po teba pošlú lietadlo.')
            print('Ale niečo za niečo... Chcú, aby si našiel faraónov [bold magenta]platinový '
                  'náhrdelník[/bold magenta], ktorý Nemci hľadajú už niekoľko mesiacov.')
            self.used = True
            context.score += 5

        return True
