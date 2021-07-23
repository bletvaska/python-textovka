from usages import use_item

from states import STATE_QUIT
from helper import get_item_by_name, get_room_by_name, show_room


def cmd_north(param: str, context: dict):
    room = context['room']
    # 1. skontrolovat, ci sa na sever da dostat. ak nie vypisem, ze: tam sa neda ist
    if room['exits']['north'] is None:
        print('Tam sa nedá isť.')
        return

    # 2. zmenit aktualnu miestnost v kontexte
    name = room['exits']['north']
    context['room'] = get_room_by_name(context['world'], name)

    # 3. zobrazim ju
    show_room(context['room'])


def cmd_south(param: str, context: dict):
    room = context['room']
    # 1. skontrolovat, ci sa na sever da dostat. ak nie vypisem, ze: tam sa neda ist
    if room['exits']['south'] is None:
        print('Tam sa nedá isť.')
        return

    # 2. zmenit aktualnu miestnost v kontexte
    name = room['exits']['south']
    context['room'] = get_room_by_name(context['world'], name)

    # 3. zobrazim ju
    show_room(context['room'])


def cmd_east(param: str, context: dict):
    room = context['room']
    # 1. skontrolovat, ci sa na sever da dostat. ak nie vypisem, ze: tam sa neda ist
    if room['exits']['east'] is None:
        print('Tam sa nedá isť.')
        return

    # 2. zmenit aktualnu miestnost v kontexte
    name = room['exits']['east']
    context['room'] = get_room_by_name(context['world'], name)

    # 3. zobrazim ju
    show_room(context['room'])


def cmd_west(param: str, context: dict):
    room = context['room']
    # 1. skontrolovat, ci sa na sever da dostat. ak nie vypisem, ze: tam sa neda ist
    if room['exits']['west'] is None:
        print('Tam sa nedá isť.')
        return

    # 2. zmenit aktualnu miestnost v kontexte
    name = room['exits']['west']
    context['room'] = get_room_by_name(context['world'], name)

    # 3. zobrazim ju
    show_room(context['room'])


def cmd_look_around(param: str, context: dict):
    show_room(context['room'])


def cmd_quit(param: str, context: dict):
    input('Naozaj chceš skončiť? (y/n) ')
    context['state'] = STATE_QUIT


def cmd_use(param: str, context: dict):
    name = param

    if name == '':
        print('Neviem čo chceš použiť.')

    else:
        items = context['room']['items'] + context['backpack']['items']
        item = get_item_by_name(items, name)

        if item is None:
            print('Takýto predmet tu nikde nevidím.')
        elif 'usable' not in item['features']:
            print('Tento predmet sa nedá použiť.')
        else:
            use_item(context, name)


def cmd_drop(param: str, context: dict):
    name = param

    if name == '':
        print('Neviem, čo chceš položiť.')

    else:
        backpack = context['backpack']
        room = context['room']

        # find item item by name
        item = get_item_by_name(backpack['items'], name)

        # if nout found
        if item is None:
            print('Taký predmet tu nigde nevidím.')
            return

        # if found
        backpack['items'].remove(item)
        room['items'].append(item)
        print(f'Do miestnosti si položil predmet {name}.')


def cmd_take(param: str,  context: dict):
    name = param
    backpack = context['backpack']

    if len(backpack['items']) >= backpack['capacity']:
        print('Batoh je plný.')

    elif name == '':
        print('Neviem, čo chceš zobrať.')

    else:
        room = context['room']

        for item in room['items']:
            if item['name'] == name:
                if 'movable' in item['features']:
                    backpack['items'].append(item)
                    room['items'].remove(item)
                    print(f'Predmet {name} si si vložil do batohu.')
                else:
                    print('Tento predmet sa nedá zobrať.')
                break

        # if no such item was found
        else:
            print('Taký predmet tu nigde nevidím.')


def cmd_explore(param: str, context: dict):
    name = param

    # if no name was given
    if name == '':
        print('Neviem, čo chceš preskúmať.')

    else:
        room = context['room']
        backpack = context['backpack']

        for item in room['items'] + backpack['items']:
            # if name was found
            if item['name'] == name:
                print(item['description'])

                # is item observable?
                if 'observable' in item['features']:
                    if item['name'] == 'chladnicka':
                        print('Zaprel si sa celou silou do dvier chladničky, '
                              'až si ich urval. Ale tá rukoväť by sa ti mohla '
                              'zísť.')
                        room['items'].append(
                            {
                                'name': 'rukovat',
                                'description': 'Kovová rukoväť značky Calex. Schopná fungovať aj ako páčidlo.',
                                'features': ['movable']
                            }
                        )
                        item['features'].remove('observable')
                break
        # if no such item was found
        else:
            print('Taký predmet tu nigde nevidím.')


def cmd_inventory(param: str, context: dict):
    backpack = context['backpack']

    if backpack['items'] == []:
        print('Batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in backpack['items']:
            print(f'\t{item["name"]}')


def cmd_commands(param: str, context: dict):
    print('Dostupné príkazy v hre:')

    for cmd in context['commands']:
        print(f'\t{cmd["name"]} - {cmd["description"]}')

    print()


def cmd_about(param: str, context: dict):
    print('Hru spáchal  (c)2021 mirek')
    print('Ďalší príbeh Indiana Jonesa sa odohráva v temnej komôrke.')
    print()
