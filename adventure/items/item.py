from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    features: list[int] = []

    def use(self, context):
        raise NotImplementedError('Usage of item was not yet implemented.')

    def examine(self, context):
        raise NotImplementedError('Examination of item was not yet implemented.')
