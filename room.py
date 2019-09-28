from exceptions import ItemNotFoundException


class Room(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._items = []
        self._exits = {}

    def set_name(self, name):
        self._name = name
        return self

    def set_description(self, description):
        self._description = description
        return self

    def set_exit(self, direction, name):
        self._exits['name'] = direction
        return self

    def add_item(self, item):
        self._items.append(item)
        return self

    def remove_item(self, name):
        for item in self._items:
            if item._name == name:
                self._items.remove(item)
                return item
        else:
            raise ItemNotFoundException('Item not found.')

    def __contains__(self, name:str):
        for item in self._items:
            if item.name == name:
                return True
        else:
            return False

    def show(self):
        print('juchu')
