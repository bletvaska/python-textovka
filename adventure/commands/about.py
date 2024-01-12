from .command import Command


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'
    # aliases = [ 'about' ]

    def exec(self, context):
        print('Hru Indiana Jones 2 napísal mladý nádejný programátor v jazyku Python - mirek v roku 2022.')
