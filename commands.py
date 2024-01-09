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


class About(Command):
    """
    Shows info about the game.
    """
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2024 created by mirek')
        print('Dalšie dobrodružstvo Indiana Jonesa tentokrát vytvorene v jazyku Python.')
