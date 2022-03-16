from directions import Directions
from items import Bucket, Matches, Door, Canister
from room import Room

world = [
    Room(name='dungeon',
         description='Nachádzaš sa v tmavej miestnosti, kde sa po stenách nachádzajú hieroglify z obdobia Juraja '
                     'Jánošíka. Valaška a krpce sú najščastejším motívom, ktorý vidíš na vyrytých postavách na stene. '
                     'Stiesňujúce miesto.',
         items=[
             Bucket(),
             Matches(),
             Canister(),
             Door()
         ]
         ),

    Room(name='garden',
         description='Zarastené ohradené miestečko naozaj len zdiaľky pripomína to, čím kedysi bolo - záhradkou. Tá '
                     'je aktuálne značne neudržiavaná a miesto reďkoviek a mrkviečik tu vidieť len lopúchy, '
                     'bodliaky a žihľavu.',
         exits={
             Directions.WEST: 'dungeon'
         }
         )
]
