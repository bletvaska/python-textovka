from exceptions import BackpackMaxCapacityReached, ItemNotFound
from items import Item


class Backpack(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._items = []

    def add(self, item: Item):
        if len(self._items) == self._capacity:
            raise BackpackMaxCapacityReached('Backpack is full.')

        self._items.append(item)

    def remove(self, name: str) -> Item:
        item = self.find_item(name)
        self._items.remove(item)
        return item

    def find_item(self, name: str) -> Item:
        for item in self._items:
            if item._name == name:
                return item
        else:
            raise ItemNotFound(f'Item "{name}" was not found in backpack.')

    def get_items(self) -> list:
        items = []
        for item in self._items:
            items.append(item._name)
        return items

    def __iter__(self):
        return self._items.__iter__()

    def __next__(self):
        return self._items.__next__()

    def __len__(self):
        return len(self._items)
