from context import Context
from .features import USABLE, MOVABLE

name = 'zapalky'

description = 'Krabička bezpečnostných zápaliek značky Billa. Zahrkal si si s nimi pri ušku, aby si sa presvedčil, ' \
              'že krabička nie je prázdna. '

features = [
    USABLE,
    MOVABLE
]


def use(context: Context):
    # 1. preconditions
    # som v miestnosti s dverami?
    # - zahrkal si zapalkami pri usku a presvedcil si sa, ze v nej naozaj nieco je.
    # su dvere su poliate benzinom?
    # *

    # 2. action
    # dvere zacnu horiet
    # - aktualizujeme popis aj nazov dveri
    # zapalky uz nebudu pouzitelne
    # - odstranime USABLE zo zapaliek
    # - aktualizujeme opis (prazdna krabicka)

    # 3. render
    print('Skrtol si zaplakou a dvere okamzite zblkli. Ak si si doteraz myslel, ze ti tu bola zima a este aj sero, '
          'tak uz to tak nie je. Je tu prijemne teplucko.')
