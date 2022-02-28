from items import door, bucket, newspaper, canister

world = {
    'kobka': {
        "description": 'Nachádzaš sa v miestnosti plnej ružových slonov. Aby si si neublížil, tak stena je pokrytá '
                       'vankúšikmi. Tiež ružovými. Žiadne okno ti neposkytne rozkošný pohľad na vonkajšiu faunu a '
                       'flóru.',
        "items": [
            door,
            bucket,
            newspaper,
            canister
        ],
        "exits": {
            'north': None,
            'south': None,
            'east': None,
            'west': None
        },
        "name": 'kobka',
    },

    'záhradka': {
        'name': 'záhradka',
        'description': 'Značne neudržiavané miesto, ktoré zrejme kedysi bolo záhradkou.',
        'items': [],
        "exits": {
            'north': None,
            'south': 'priekopa',
            'east': 'kobka',
            'west': None
        },
    },

    'priekopa': {
        'name': 'priekopa',
        'description': 'Nedával si si pozor a rovno si čľupol medzi aligátory. Čo tu robia na Slovensku také '
                       'ušľachtilé tvory? Pomyslel si si. Čo tu robí taký výdatný štyridsiatnik? Pomysleli si oni. '
                       'A nerozmýšľali o tom dlho.',
        'items': [],
        "exits": {
            'north': None,
            'south': None,
            'east': None,
            'west': None
        },

    }
}
