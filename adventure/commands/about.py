from .command import Command


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, context):
        print('(c)2024 ukradol mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentokrát s jazykom Python.')
