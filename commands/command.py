from pydantic import BaseModel

from game_context import GameContext


class Command(BaseModel):
    """
    Generic command of the game.
    """
    # fields
    name: str
    description: str
    param: str = None

    # methods
    def exec(self, context: GameContext):
        raise NotImplementedError('This method was not yet implemented.')
