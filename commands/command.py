from exceptions import CommandNotYetImplemented


class Command:
    def __init__(self, name: str, description: str):
        self._name = name.lower()
        self._description = description.lower()
        self._params = None

    def exec(self, context):
        raise CommandNotYetImplemented('Telo príkazu ešte nebolo implementované.')

    def __str__(self):
        return f'{self._name.upper()} - {self._description}'

    def save_to_history(self, context):
        if self._params is not None:
            context.history.append(f'{self._name} {self._params}')
        else:
            context.history.append(self._name)
