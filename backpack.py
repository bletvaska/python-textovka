from exceptions import FullBackpackException, ItemNotFoundException
from items import Item


class Backpack(object):
    """
    Class represents player's backpack.
    There is also an example of usage magic methods __len__(), __iter__() and __next__().
    """

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._items = []

    def add_item(self, item: Item):
        """
        Adds item to backpack, if there is space.
        If there is no space for additional item, exception FullBackpackException raises.
        :param item: item to add
        """
        if len(self._items) == self._capacity:
            raise FullBackpackException('Backpack is full.')

        self._items.append(item)

    # def find_item(self, name: str) -> Item:
    #     """
    #     Find's item in backpack.
    #     If the item can't be found, ItemNotFoundException raises. Otherwise the founded item is returned.
    #     :param name: name of item to find
    #     :return: item object
    #     """
    #     for item in self._items:
    #         if item.name == name:
    #             return item
    #     else:
    #         raise ItemNotFoundException('Item was not found in backpack.')

    def remove_item(self, name: str) -> Item:
        """
        Removes item from backpack.
        If the item is not in backpack, ItemNotFoundException raises. Otherwise the item is removed from backpack and
        it is returned.
        :param name: name of the item to remove
        :return: the removed item object
        """
        item = self[name]
        self._items.remove(item)
        return item

    def __len__(self):
        """
        Provides support for built-in len() function.
        :return: Number of items in backpack
        """
        return len(self._items)

    # implementation of Iterator Design Pattern
    def __iter__(self):
        return self._items.__iter__()

    def __next__(self):
        return self._items.__next__()

    def __getitem__(self, name:str):
        """
        Allows to use backpack['name'] to get item.
        :param name: name of item
        :return: item object
        """
        for item in self._items:
            if item.name == name:
                return item
        else:
            raise ItemNotFoundException(f'"{name}" sa v batohu nenachádza.')

    def __contains__(self, name:str):
        for item in self._items:
            if item.name == name:
                return True
        else:
            return False
