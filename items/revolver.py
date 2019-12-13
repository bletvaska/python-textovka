from items import Item, mixins


class Revolver(Item, mixins.Movable):
    def __init__(self):
        super().__init__('revolver', 'Revolver na strieľanie.')