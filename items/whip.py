from items import Item, mixins


class Whip(Item, mixins.Movable):
    def __init__(self):
        super().__init__('bic', 'Bičík na šľahanie.')
