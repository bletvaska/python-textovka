from dataclasses import dataclass


@dataclass
class Command:
    # fields
    name: str
    description: str

    # behavior / methods
    def exec(self):
        print('vykonavam prikaz')


# * prikazy
#   * opis
#   * nazov
#   * aliasy
#   // * parameter (vezmi revolver)
#   + vykonanie prikazu(item)
