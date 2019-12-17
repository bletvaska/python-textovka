from items import Item


class Whip(Item):
    def __init__(self):
        super().__init__('bic', 'Bičík na šľahanie.', ['movable'])
