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

# * prikazy
#   * opis
#   * nazov
#   * aliasy
#   // * parameter (vezmi revolver)
#   + vykonanie prikazu(item)
