from pydantic import BaseModel

from context import Context


class Command(BaseModel):
    """
    Generic game command.
    """
    # fields
    name: str
    description: str
    param = ''

    # methods
    def exec(self, context: Context):
        raise NotImplementedError('This method was not yet implemented.')
