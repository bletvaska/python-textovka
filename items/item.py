class Item(object):
    def __init__(self, name, description, features):
        self._name = name
        self._description = description
        self._features = features

    def __str__(self):
        return f'{self._name} - {self._description}'