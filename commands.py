

from usables import use_bucket, use_canister, use_matches
from helper import show_room


def cmd_about():
    print('(c)2021 by mirek na mocnom Pythoňáckom kurze spáchal.')
    print('Táto mocná hra je o...')


def cmd_inventory(context):
    backpack = context['backpack']

    if len(backpack) == 0:
        print('Batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in backpack:
            print(f'  {item["name"]}')


def cmd_commands():
    print('Zoznam akutálne dostupných príkazov:')
    print('o hre - zobrazí informácie o hre')
    print('koniec - ukončí hru')
    print('prikazy - zobrazi zoznam prikazov')
    print('zapad - prejdeš na západ')
    print('rozhliadni sa - zobrazí opis aktuálnej miestnosti')


def cmd_look_around(context):
    show_room(context['current_room'])


def cmd_explore(context):
    backpack = context['backpack']
    current_room = context['current_room']
    line = context['line']

    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print('Čo chceš preskúmať?')
    else:
        name = cmd[1]

        for item in current_room['items'] + backpack:
            if item['name'] == name:
                print(item['description'])
                break
        else:
            print('Taký predmet tu nikde nevidím.')


def cmd_drop(context):
    backpack = context['backpack']
    current_room = context['current_room']
    line = context['line']

    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print('Neviem, čo chceš položiť.')
    else:
        name = cmd[1]
        found = False
        for item in backpack:
            if item['name'] == name:
                backpack.remove(item)
                current_room['items'].append(item)
                print(f'Do miestnosti si položil {item["name"]}.')
                found = True
                break
        if found == False:
            print('Taký predmet u seba nemáš.')


def cmd_take(context):
    current_room = context['current_room']
    backpack = context['backpack']
    line = context['line']

    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print('Neviem, čo chceš zobrať.')
    else:
        name = cmd[1]
        found = False
        for item in current_room['items']:

            if item['name'] == name:
                if 'movable' in item['features']:
                    current_room['items'].remove(item)
                    backpack.append(item)
                    print(f'Do batohu si vložil {item["name"]}.')
                else:
                    print('Tento predmet sa nedá zobrať.')

                found = True
                break

        if found == False:
            print(
                f'Taký predmet v miestnosti {current_room["name"]} nevidím.')


def cmd_use(context):
    current_room = context['current_room']
    backpack = context['backpack']
    line = context['line']

    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print('Co chces pouzit?')
    else:
        name = cmd[1]
        found = False
        for item in current_room['items'] + backpack:
            if item['name'] == name:
                if 'usable' in item['features']:
                    if name == 'kanister':
                        use_canister(item, current_room)

                    elif name == 'zapalky':
                        use_matches(current_room, backpack)

                    elif name == 'vedro':
                        use_bucket(current_room, backpack, item)

                else:
                    print((f'{item["name"]} sa neda pouzit.').capitalize())

                found = True
                break
        if found == False:
            print('Taky predmet tu nikde nevidim.')


def cmd_east(context):
    name = context['current_room']['exits']['east']
    if name != None:
        context['current_room'] = context['world'][name]
        show_room(context['world'][name])
    else:
        print('Tam sa nedá ísť.')


def cmd_west(context):
    name = context['current_room']['exits']['west']
    if name != None:
        context['current_room'] = context['world'][name]
        show_room(context['current_room'])
    else:
        print('Tam sa nedá ísť.')


def cmd_north(context):
    name = context['current_room']['exits']['north']
    if name != None:
        context['current_room'] = context['world'][name]
        show_room(context['current_room'])
    else:
        print('Tam sa nedá ísť.')


def cmd_south(context):
    name = context['current_room']['exits']['south']
    if name != None:
        context['current_room'] = context['world'][name]
        show_room(context['current_room'])
    else:
        print('Tam sa nedá ísť.')
