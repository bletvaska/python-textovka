class Item:
    def __init__(self, name: str, description: str):
        self._name = name.lower()
        self._description = description.capitalize()

    def __str__(self):
        return f'{self._name} - {self._description}'
