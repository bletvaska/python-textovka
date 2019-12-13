from items import Item


class Backpack:
    def __init__(self, capacity: int = 2):
        self._capacity = capacity
        self._items = []

    def append(self, item):
        if len(self._items) >= self._capacity:
            print('Batoh je plný.')
            return

        self._items.append(item)

    def get(self, name):
        for item in self._items:
            if item._name == name:
                return item
        else:
            return None

    def remove(self, item: Item):
        self._items.remove(item)

    def list(self):
        for item in self._items:
            print(item._name)
