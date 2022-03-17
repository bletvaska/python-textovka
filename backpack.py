from dataclasses import dataclass, field


class AdventureException(Exception):
    pass


class FullBackpack(AdventureException):
    pass


class ItemNotFound(AdventureException):
    pass


@dataclass
class Backpack:
    items: list = field(default_factory=list)
    capacity: int = 2
    _index: int = 0

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return self.items.__iter__()

    # def __next__(self):
    #     if self._index >= len(self.items):
    #         self._index = 0
    #         raise StopIteration
    #
    #     self._index += 1
    #     return self.items[self._index - 1]

    def __getitem__(self, key):
        for item in self.items:
            if item == key:
                return item

        raise ItemNotFound(f'Item {key} was not found in backpack.')

    def get(self, key):
        return self.__getitem__(key)

    def append(self, item):
        if len(self.items) == self.capacity:
            raise FullBackpack('Backpack is full.')

        self.items.append(item)

    def __str__(self):
        if self.items == []:
            return 'Batoh je prázdny.'
        else:
            output = "V batohu máš:\n"
            for item in self.items:
                output += f'\t* {item.name}'
            return output
