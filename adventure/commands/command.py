from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic game command.
    """
    name: str
    description: str

    def exec(self, backpack: list, commands: list) -> str:
        raise NotImplementedError(f'This method was not yet implemented for command {self.name}.')
