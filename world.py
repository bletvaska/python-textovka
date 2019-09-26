from items import GoldenIdol, Branch

world = {
    'pred jaskynou': {
        'name': 'pred jaskynou',
        'description': "Stojis pred vchodom do tajomnej jaskyne. Jaskyna nevesti nic dobre.",
        'exits': {
            'vychod': 'v jaskyni'
        },
        'items': []
    },

    'v jaskyni': {
        'name': 'v jaskyni',
        'description': 'Stojis v temnej jaskyni. Uz aj tak mizernu viditelnost znizuju este pavuciny, ktorych je tu teda riadna kopa.',
        'exits': {
            'zapad': 'pred jaskynou',
            'vychod': 'nad priepastou'
        },
        'items': []
    },

    'nad priepastou': {
        'name': 'nad priepastou',
        'description': 'Okrem pavucin a nahodne skakjucich tarantul tu nie je nic zaujimave. Pokial za zaujimave nepokladas tu priepast, ktora zabera vacsinu vyhladu v tejto miestnosti.',
        'exits': {
            'zapad': 'v jaskyni',
            'dolu': 'priepast',
            # 'vychod': 'chram'
        },
        'items': [
            Branch()
        ]
    },

    'priepast': {
        'name': 'priepast',
        'description': 'Dno priepaste posiate kostrami rozlicneho vzrastu. Zrejme sa jedna o nahodnych turistov, ktori svoj vylet nestihli dokoncit. Alebo len preskocit.',
        'exits': {},
        'items': []
    },

    'chram': {
        'name': 'chram',
        'description': 'Rozlahla miestnost, v strede ktorej sa nachadza oltar, na ktorom je este stale umiestneny ciel tvojej cesty: Golden Idol.',
        'exits': {
            'zapad': 'nad priepastou'
        },
        'items': [
            GoldenIdol()
        ]
    }
}
