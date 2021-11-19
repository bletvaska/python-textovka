SOAKED = 'soaked'
NORMAL = 'normal'
BURNING = 'burning'

normal = {
    'name': 'dvere',
    'description': 'Veľké masívne dubové dvere. Len tak niečo a niekto s nimi nepohne, keď sú zamknuté. A to teda sú.',
    'features': [],
    'state': NORMAL
}

soaked = {
    'name': 'dvere',
    'description': 'Veľké masívne dubové dvere. Len tak niečo a niekto s nimi nepohne, keď sú zamknuté. A to teda sú. A ešte k tomu aj parádne nasiaknuté vysokooktánovým benzínom.',
    'features': [],
    'state': SOAKED
}

burning = {
    'name': 'horiace dvere',
    'description': 'Veľké masívne dubové dvere zachvátené obrovským výdatným plameňom.',
    'features': [],
    'state': BURNING
}


def change_state(state: str):
    if state == NORMAL:
        pass
    elif state == SOAKED:
        pass
    elif state == BURNING:
        pass
    # else:
    #     raise