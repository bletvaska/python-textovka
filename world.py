world = [
    {
        'description': 'Nachádzaš v tmavej miestnosti. Kamenné múry dávajú tušiť, že sa nachádzaš v nejakej kamennej kobke. Žeby podzemie hradu v Grunwalde? Okná tu nie sú žiadne, čo by ťa uistili o správnosti tohto predpokladu.',
        'name': 'chamber',
        'items': [
            {
                'name': 'vedro',
                'description': 'Vedro plné vody.',
                'features': ['movable', 'usable']
            },
            {
                'name': 'kanister',
                'description': 'Kanister plný benzínu.',
                'features': ['movable', 'usable']
            },
            {
                'name': 'zapalky',
                'description': 'Zápalky na vatru.',
                'features': ['movable', 'usable'],
                'attempts': 3
            },
            {
                'name': 'chladnicka',
                'description': 'Chladnička značky Calex. Zvláštne znamenie: pokazená.',
                'features': ['observable']
            },
            {
                'name': 'dvere',
                'description': 'Veľké masívne dubové dvere.',
                'features': []
            }
        ],
        'exits': {
            'north': None,
            'south': None,
            'east': None,
            'west': None
        }
    },

    {
        'description': 'Hala s kamennými stenami, na ktorých je svastikou napísané Wilcommen tu Grunwalt.',
        'name': 'hall',
        'items': [],
        'exits': {
            'north': None,
            'south': 'chamber',
            'east': None,
            'west': None
        }
    }

]
