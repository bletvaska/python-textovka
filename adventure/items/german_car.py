from .car_battery import CarBattery
from .features import EXAMINABLE
from .item import Item


class GermanCar(Item):
    name = 'nemecky automobil'
    description = 'Mercedes Benz, ale bohužiaľ v nepojazdnom stave.'
    features = [EXAMINABLE]

    def examine(self, context):
        # action
        context.current_room.items.append(CarBattery())
        self.features.remove(EXAMINABLE)

        # render
        print('V kufri auta si objavil batériu!')
