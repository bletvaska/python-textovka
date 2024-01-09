from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic command of the game.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self):
        print("ta vykonavam prikaz ", self.name)
