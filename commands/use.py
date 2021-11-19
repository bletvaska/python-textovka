from helpers import get_item_by_name
from items import USABLE


def _exec(context: dict, param: str):
    name = param

    # if the name was not entered
    if name == '':
        print('Neviem, aký predmet chceš použiť.')
        return

    # search for item in backpack items
    item = get_item_by_name(name, context['room']['items'] + context['backpack']['items'])

    # item not found
    if item is None:
        print('Taký predmet tu nikde nevidim.')
        return

    # item is not usable
    elif USABLE not in item['features']:
        print('Tento predmet sa nedá použiť.')
        return

    # check if item has use key
    if 'use' not in item:
        raise NotImplementedError()

    # save to history
    context['history'].append(f'{cmd["name"]} {param}')

    # use item
    item['use'](context)


cmd = {
    'name': "pouzi",
    'description': 'použi predmet nachádzajúci sa v miestnosti alebo v batohu',
    'aliases': ("use",),
    'exec': _exec,
}
