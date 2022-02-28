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

    'zahradka': {
        'name': 'záhradka',
        'description': 'Značne neudržiavané miesto, ktoré zrejme kedysi bolo záhradkou.',
        'items': [],
        "exits": {
            'north': None,
            'south': None,
            'east': None,
            'west': None
        },
    }
}
