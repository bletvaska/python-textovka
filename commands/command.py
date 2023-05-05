from pydantic import BaseModel

from game_context import GameContext


class Command(BaseModel):
    name: str
    description: str
    param: str | None = None

    def exec(self, context: GameContext):
        raise NotImplementedError('Function exec() was not yet implemented.')
