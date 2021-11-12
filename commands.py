import states
from items import MOVABLE


def cmd_about(context):
    print('(c)2021 created by mirek')
    print('Ďalšie veľké dobrodružstvo Indiana Jonesa. Tentokrát zápasí s jazykom Python v tmavej miestnosti.')


def cmd_commands(context):
    print('Zoznam príkazov v hre:')
    print('* koniec - ukončí rozohratú hru')
    print('* o hre - zobrazí informácie o hre')
    print('* poloz - polozi zvoleny predmet v miestnosti')
    print('* prikazy - zobrazí príkazy, ktoré sa dajú použiť v hre')
    print('* rozhliadni sa - vypíše opis miestnosti, v ktorej sa hráč práve nachádza')
    print('* vezmi - vezme predmet z miestnosti a vloží si ho do batohu')


def cmd_show_inventory(context):
    if context['backpack']['items'] == []:
        print("Batoh je prázdny.")
    else:
        print("V batohu máš:")
        for item in context['backpack']['items']:
            print(f"   * {item['name']}")


def cmd_drop_item(line, context):
    backpack = context['backpack']
    room = context['room']
    name = line.split('poloz')[1].strip()

    # if the name was not entered
    if name == '':
        print('Neviem, čo chceš položiť.')

    else:
        # search for item in room items
        for item in backpack['items']:
            if name == item['name']:
                # take item
                backpack['items'].remove(item)
                room['items'].append(item)
                print(f'Do miestnosti si položil predmet {name}.')
                break

        # item not found
        else:
            print('Taký predmet pri sebe nemáš.')


def cmd_take_item(line, context):
    backpack = context['backpack']
    room = context['room']
    name = line.split('vezmi')[1].strip()

    # if the name was not entered
    if name == '':
        print('Neviem, čo chceš zobrať.')

    else:
        # search for item in room items
        for item in room['items']:
            # found item
            if name == item['name']:
                # is the item movable?
                if MOVABLE in item['features']:
                    # is backpack full?
                    if len(backpack['items']) >= backpack['max']:
                        print('Batoh je plný')
                        break
                    else:
                        # take item
                        room['items'].remove(item)
                        backpack['items'].append(item)
                        print(f'Do batohu si si vložil predmet {name}.')
                else:
                    print('Tento predmet sa nedá vziať.')
                break

        # item not found
        else:
            print('Taký predmet tu nikde nevidím.')


def cmd_quit(context):
    context['state'] = states.QUIT
