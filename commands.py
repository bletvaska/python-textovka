from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic game command.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self):
        print('vykonavam prikaz ', self.name)


class About(Command):
    # fields
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2023 created by mirek')
        print('Dalšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')
