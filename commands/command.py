from pydantic import BaseModel


class Command(BaseModel):
    name: str
    description: str

    def exec(self, context):
        raise NotImplementedError('This method is not implemented.')
