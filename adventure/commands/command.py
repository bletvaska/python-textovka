from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic game command.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self, context) -> str:
        raise NotImplementedError('This method was not yet implemented.')
