from helpers import get_item_by_name


def _exec(context: dict, param: str):
    name = param

    # if the name was not entered
    if name == '':
        print('Neviem, čo chceš preskúmať.')
        return

    # search for item in room items
    item = get_item_by_name(name, context['room']['items'] + context['backpack']['items'])

    # item not found
    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    # show item description
    print(item['description'])


cmd = {
    'name': "preskumaj",
    'description': 'zobrazí opis daného predmetu',
    'aliases': ("examine",),
    'exec': _exec,
}
