class Item(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def __str__(self):
        return f'{self._name} - {self._description}'