from pydantic import BaseModel


class Command(BaseModel):
    name: str
    description: str

    def exec(self, backpack, commands):
        raise NotImplementedError('This method is not implemented.')
