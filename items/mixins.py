from abc import ABC, abstractmethod
from game_context import GameContext

"""
Abstract classes specified the item mixins/features.
"""


class MovableMixin(ABC):
    """
    Movable items can be carried in backpack.
    """
    pass


class UsableMixin(ABC):
    """
    Usable items can be used in some specific scenarios.
    """
    @abstractmethod
    def use(self, context: GameContext):
        pass
