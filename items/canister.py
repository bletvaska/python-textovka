from dataclasses import dataclass

from items.features import MOVABLE, USABLE


@dataclass
class Canister:
    name = 'kanister'
    description = 'Veľký 25l kanister. Po odšróbovaní vrchnáka si zistil, že je to benzín. Kvalitka. 98 oktánov.'
    features = [USABLE, MOVABLE]
