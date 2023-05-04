from pydantic import BaseModel


class Room(BaseModel):
    name: str
    description: str
    items: list = []
    exits: list = []


class Airplane(Room):
    name = 'v lietadle'
    description = 'Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory stoja a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že ano?)'
    items = ['bic', 'prazdne sedadla']
