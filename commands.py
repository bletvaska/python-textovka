from dataclasses import dataclass


@dataclass
class Command:
    # fields
    name: str
    description: str

    # behavior / methods
    def exec(self):
        print('vykonavam prikaz')


@dataclass
class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        print('Hru Indiana Jones 2 napísal mladý nádejný programátor v jazyku Python - mirek v roku 2022.')


@dataclass
class Commands(Command):
    # fields
    name: str = 'prikazy'
    description: str = 'zobrazí dostupné príkazy v hred'

    # methods
    def exec(self):
        print('V hre je možné použiť tieto príkazy:')
        print('* inventar - zobrazi obsah hráčovho batohu')
        print('* koniec - ukončí hru')
        print('* o hre - zobrazi informacie o hre')
        print('* prikazy - zoznam dostupných príkazov v hre')

# * prikazy
#   * opis
#   * nazov
#   * aliasy
#   // * parameter (vezmi revolver)
#   + vykonanie prikazu(item)
