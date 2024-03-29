from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from game_context import GameContext

from pydantic import BaseModel


class Command(BaseModel):
    """
    Describes every command in game.
    """
    name: str
    aliases: List[str] = []
    description: str
    param: str = None

    def exec(self, context: "GameContext") -> None:
        raise NotImplemented(f'Príkaz {self.name} ešte nebol implementovaný.')
