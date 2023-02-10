from .features import MOVABLE
from .item import Item


class Diamond(Item):
    name = 'diamant'
    description = 'Ťažký, neforemný drahý kameň.'
    features = [MOVABLE]

    def on_drop(self, context):
        if context.current_room.name == 'oltár':
            print('Žiarenie oltára ešte viac zosilnelo.')
