from pydantic import BaseModel

from game_context import GameContext


class Command(BaseModel):
    """
    Generic game command.
    """
    name: str
    description: str

    def exec(self, context: GameContext):
        raise NotImplementedError(f'This method was not yet implemented for command {self.name}.')
