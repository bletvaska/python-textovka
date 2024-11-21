from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic game command.
    """
    name: str
    description: str

    def exec(self):
        print(f'vykonavam prikaz {self.name}')


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2024 ukradol mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentokrát s jazykom Python.')


class Quit(Command):
    pass


class Commands(Command):
    pass
