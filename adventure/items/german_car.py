from rich import print

from .car_battery import CarBattery
from .features import EXAMINABLE
from .item import Item


class GermanCar(Item):
    name: str = 'nemecky automobil'
    description: str = 'Mercedes Benz, ale bohužiaľ v nepojazdnom stave.'
    features: list[int] = [EXAMINABLE]

    def on_examine(self, context):
        # action
        context.current_room.items.append(CarBattery())

        # post-processing
        context.score += 5
        self.features.remove(EXAMINABLE)

        # render
        print('V kufri auta si objavil [bold magenta]batériu[/bold magenta]!')
