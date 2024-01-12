from .features import MOVABLE
from .item import Item


class Diamond(Item):
    name: str = 'diamant'
    description: str = 'Ťažký, neforemný drahý kameň.'
    features: list[int] = [MOVABLE]

    def on_drop(self, context):
        if context.current_room.name == 'oltár':
            print('Žiarenie oltára ešte viac zosilnelo.')
