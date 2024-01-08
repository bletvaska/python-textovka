from .command import Command


class About(Command):
    name = 'o hre'
    description = 'zobrazí informácie o hre'
    # aliases = [ 'about' ]

    def exec(self, context):
        print('Hru Indiana Jones 2 napísal mladý nádejný programátor v jazyku Python - mirek v roku 2022.')
