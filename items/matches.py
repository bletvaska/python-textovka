from context import Context
from helpers import get_item_by_name
from .features import USABLE, MOVABLE

name = 'zapalky'

description = 'Krabička bezpečnostných zápaliek značky Billa. Zahrkal si si s nimi pri ušku, aby si sa presvedčil, ' \
              'že krabička nie je prázdna.'

features = [
    USABLE,
    MOVABLE
]


def use(context: Context):
    # 1. preconditions
    # som v miestnosti s dverami?
    door = get_item_by_name('dvere', context.room['items'])
    if door is None:
        print('zahrkal si zapalkami pri usku a presvedcil si sa, ze v nej naozaj nieco je.')
        return

    # su dvere su poliate benzinom?
    if door.state != door.SOAKED_STATE:
        print('Hmm... To mi nejako nevychádza. Si istý, že tie drevené dvere len tak podpáliš jednou zápalkou?')
        return

    # 2. action
    # dvere zacnu horiet

    # - aktualizujeme popis aj nazov dveri
    door.name = 'horiace dvere'
    door.description = 'Veľké dubové masívne horiace dvere.'
    door.state = door.BURNING_STATE

    # zapalky uz nebudu pouzitelne
    # - odstranime USABLE zo zapaliek
    features.remove(USABLE)
    # - aktualizujeme opis (prazdna krabicka)
    global description
    description = 'Prázdna krabička bezpečnostných zápaliek značky Billa.'

    # 3. render
    print('Skrtol si zapalkou a dvere okamzite zblkli. Ak si si doteraz myslel, ze ti tu bola zima a este aj sero, '
          'tak uz to tak nie je. Je tu prijemne teplucko.')
