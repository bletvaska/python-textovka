from .command import Command


class About(Command):
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self, context):
        print('Túto mocnú hru spáchal mocný programátor mirek')
        print('(c)2023 by mirek')
