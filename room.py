class Room:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._exits = {}

    def add_exit(self, name, room):
        if isinstance(room, Room):
            self._exits[name] = room
        else:
            raise TypeError('Not a Room object.')


    def __str__(self) -> str:
        return self._description

    def __repr__(self):
        return f'repr: "{self._name}". {self._description}'