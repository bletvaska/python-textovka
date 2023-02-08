from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic game command.
    """
    # fields
    name: str
    description: str
    param = ''

    # methods
    def exec(self, context):
        raise NotImplementedError('This method was not yet implemented.')
