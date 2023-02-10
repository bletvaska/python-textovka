from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    features = []

    def use(self, context) -> bool:
        return False

    def on_drop(self, context):
        pass
