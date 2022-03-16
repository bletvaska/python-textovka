from items import Bucket, Matches, Door, Canister

world = [
    {
        'name': 'dungeon',
        'description': 'Nachádzaš sa v tmavej miestnosti, kde sa po stenách nachádzajú hieroglify z obdobia Juraja Jánošíka. Valaška a krpce sú najščastejším motívom, ktorý vidíš na vyrytých postavách na stene. Stiesňujúce miesto.',
        'items': [
            Bucket(),
            Matches(),
            Canister(),
            Door()
        ],
        'exits': {
            'east': None,
            'west': None,
            'north': None,
            'south': None
        }
    },

    {
        'name': 'garden',
        'description': 'Zarastené ohradené miestečko naozaj len zdiaľky pripomína to, čím kedysi bolo - záhradkou. Tá je aktuálne značne neudržiavaná a miesto reďkoviek a mrkviečik tu vidieť len lopúchy, bodliaky a žihľavu.',
        'items': [],
        'exits': {
            'north': None,
            'south': None,
            'east': None,
            'west': 'dungeon'
        }
    },

]
