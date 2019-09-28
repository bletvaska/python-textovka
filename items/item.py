from abc import ABC


class Item(ABC):
    """
    Abstract class specifying game item.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description}'
