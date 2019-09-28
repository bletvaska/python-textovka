from abc import ABC, abstractmethod

from game_context import GameContext


class Command(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.params = None
        self.aliases = [name]

    @abstractmethod
    def exec(self, context: GameContext):
        pass

    def __str__(self):
        return f'{self.name} - {self.description}'
