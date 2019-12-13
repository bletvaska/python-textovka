from items import Item, mixins


class Fedora(Item, mixins.Movable):
    def __init__(self):
        super().__init__('klobuk', 'Klobúčik na hlavičku.')