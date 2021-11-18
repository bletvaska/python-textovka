from helpers import get_item_by_name


def _exec(context: dict, param: str):
    backpack = context['backpack']
    room = context['room']
    name = param

    # if the name was not entered
    if name == '':
        print('Neviem, čo chceš položiť.')
        return

    # search for item in backpack items
    item = get_item_by_name(name, backpack['items'])

    # item not found
    if item is None:
        print('Taký predmet pri sebe nemáš.')
        return

    # drop item
    backpack['items'].remove(item)
    room['items'].append(item)
    print(f'Do miestnosti si položil predmet {name}.')


cmd = {
    'name': "poloz",
    'description': 'položí zvolený predmet v miestnosti',
    'aliases': ("drop",),
    'exec': _exec,
}
