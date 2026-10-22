from commands.base import BaseCommand


class About(BaseCommand):
    name = 'o hre'
    description = 'Zobrazí informácie o hre.'

    def exec(self):
        print('(c)2026 created by mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')
