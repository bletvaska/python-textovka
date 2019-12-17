class Item:
    def __init__(self, name: str, description: str, features: list = None):
        self._name = name.lower()
        self._description = description.capitalize()
        self.features = []
        if features is not None:
            self.features += features

    def __str__(self):
        return f'{self._name} - {self._description}'
