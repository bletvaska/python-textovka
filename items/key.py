from items import Item


class Key(Item):
    def __init__(self):
        super().__init__('klucik', 'Veľmi používaný kľúčik značky FAB.', ['movable'])