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

    def __len__(self):
        return len(self._items)

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError('Not an Item')

        if len(self._items) >= self._capacity:
            raise Exception('Backpack si full.')

        self._items.append(other)

        return self

    def __sub__(self, other):
        if not isinstance(other, Item):
            raise TypeError('Not an Item.')

        self._items.remove(other)

        return self

    def __contains__(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Not a string.')

        for item in self._items:
            if item._name == name:
                return True

        return False

    def __getitem__(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Not a string.')

        for item in self._items:
            if item._name == name:
                return item

        raise KeyError('Not in backpack.')

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self._items):
            raise StopIteration
        item = self._items[self.index]
        self.index += 1
        return item._name
