from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_context import GameContext
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    features: list = []

    def on_use(self, context: 'GameContext'):
        return False

    def on_examine(self, context: 'GameContext'):
        pass

    def on_drop(self, context: 'GameContext'):
        pass

    def __str__(self):
        return self.name
