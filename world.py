from items import canister, matches, fire_extinguisher, newspaper, door


world = [
    {
        'name': 'dungeon',
        'description': 'Nachádzaš sa v tmavej zatuchnutej miestnosti. Na kamenných stenách sa nenachádza žiadne okno, '
                       'čo dáva tušiť, že si niekoľko metrov pod zemou. Žeby košický hrad? Aj to je možné, ti '
                       'prebleslo hlavou.',
        'items': [
            canister,
            matches,
            fire_extinguisher,
            newspaper,
            door
        ],
        'exits': {
            'west': None,
            'south': None,
            'north': None,
            'east': None
        }
    },

    {
        'name': 'garden',
        'description': 'Značne neudržiavaný priestor, ktorý sa určite pred pár rokmi volal záhradka.',
        'items': [
        ],
        'exits': {
            'west': 'dungeon',
            'south': None,
            'north': None,
            'east': None
        }
    },
]
