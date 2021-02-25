

from helper import show_room


def cmd_about():
    print('(c)2021 by mirek na mocnom Pythoňáckom kurze spáchal.')
    print('Táto mocná hra je o...')


def cmd_inventory(backpack):
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


def cmd_look_around(current_room):
    show_room(current_room)


def cmd_explore(backpack, current_room, line):
    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print('Čo chceš preskúmať?')
    else:
        name = cmd[1]

        found = False
        for item in current_room['items'] + backpack:
            if item['name'] == name:
                print(item['description'])
                found = True
                break

        if found == False:
            print('Taký predmet tu nikde nevidím.')


def cmd_drop(backpack, current_room, line):
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


def cmd_take(backpack, current_room, line):
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


def cmd_use(backpack, current_room, line):
    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print('Co chces pouzit?')
    else:
        name = cmd[1]
        found = False
        for item in current_room['items'] + backpack:
            if item['name'] == name:
                if 'usable' in item['features']:
                    print(f'Pouzivam predmet {item["name"]}')
                else:
                    print((f'{item["name"]} sa neda pouzit.').capitalize())

                found = True
                break
        if found == False:
            print('Taky predmet tu nikde nevidim.')


def cmd_east(room, world):
    name = room['exits']['east']
    if name != None:
        room = world[name]
        show_room(room)
    else:
        print('Tam sa nedá ísť.')

    return room


def cmd_west(current_room, world):
    name = current_room['exits']['west']
    if name != None:
        current_room = world[name]
        show_room(current_room)
    else:
        print('Tam sa nedá ísť.')

    return current_room


def cmd_north(current_room, world):
    name = current_room['exits']['north']
    if name != None:
        current_room = world[name]
        show_room(current_room)
    else:
        print('Tam sa nedá ísť.')

    return current_room


def cmd_south(current_room, world):
    name = current_room['exits']['south']
    if name != None:
        current_room = world[name]
        show_room(current_room)
    else:
        print('Tam sa nedá ísť.')

    return current_room
