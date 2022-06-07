from items.bucket import Bucket
from items.canister import Canister
from items.door import Door
from items.matches import Matches
from room import Room

world = [
    Room(
        name='dungeon',
        description='Stojíš uprostred chladnej kamennej miestnosti, v ktorej nie sú žiadne okná.',
        items=[
            Door(),
            Bucket(),
            Canister(),
            Matches()
        ]
    ),

    Room(
        name='garden',
        description=('Malá evidentne neudržiavaná záhradka. '
                     'Tá burina, čo tu rastie, mali asi pôvodne byť záhony pre fazuľku.')
    )
]
