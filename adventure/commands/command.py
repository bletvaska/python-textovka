from pydantic import BaseModel

from rooms import Room


class Command(BaseModel):
    """
    Generic game command.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self, room: Room, commands: list) -> str:
        raise NotImplementedError('This method was not yet implemented.')
