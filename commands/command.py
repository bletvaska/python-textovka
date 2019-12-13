from exceptions import CommandNotYetImplemented


class Command:
    def __init__(self, name: str, description: str):
        self._name = name.lower()
        self._description = description.lower()

    def exec(self, context):
        raise CommandNotYetImplemented('Telo príkazu ešte nebolo implementované.')
