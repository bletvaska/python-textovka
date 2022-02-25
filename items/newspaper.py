import random

from .features import USABLE, MOVABLE

name = 'noviny'

description = 'Čerstvé vydanie liberálneho denníka plného americkej nenávisti Denník N.'

features = [
    USABLE,
    MOVABLE
]


def use():
    print('Zalistoval si si v novinách a začítal si sa')

    headlines = [
        'Tri steniatky najdene po troch dnoch nezvestnosti',
        'Matka predala vlastny byt. Zostali jej oci pre plac',
        'Radost v Kosiciach. Novy stadion otvoreny',
        'Macky boli pravymi vladcami Egypta, tvrdi historik',
        'Klobuky ktore sa hodia na vsetky mudre hlavy'
    ]

    print(random.choice(headlines))
