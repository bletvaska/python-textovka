from items import Item, mixins


class RubberBoat(Item, mixins.Movable):
    def __init__(self):
        super().__init__('gumenny cln', 'Gumenný čln na plávanie.')