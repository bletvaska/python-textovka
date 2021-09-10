import random

import features
from helper import find_item


def use_textbook(item, context):
    _zen_of_python = [
        'Beautiful is better than ugly.',
        'Explicit is better than implicit.',
        'Simple is better than complex.',
        'Complex is better than complicated.',
        'Flat is better than nested.',
        'Sparse is better than dense.',
        'Readability counts.',
        "Special cases aren't special enough to break the rules.",
        'Although practicality beats purity.',
        'Errors should never pass silently.',
        'Unless explicitly silenced.',
        'In the face of ambiguity, refuse the temptation to guess.',
        'There should be one-- and preferably only one --obvious way to do it.',
        "Although that way may not be obvious at first unless you're Dutch.",
        'Now is better than never.',
        'Although never is often better than *right* now.',
        "If the implementation is hard to explain, it's a bad idea.",
        'If the implementation is easy to explain, it may be a good idea.',
        "Namespaces are one honking great idea -- let's do more of those!",
    ]

    print('Zalistoval si v učebnici a dočítal si sa, že:')
    print(random.choice(_zen_of_python))


def use_can(item, context):
    room = context['room']

    # aktualizovali sme kanister
    item['description'] = 'Prázdny kanister. Po pričuchnutí je ti to jasné - bol tu benzín.'
    item['features'].remove(features.USABLE)

    # aktualizujeme dvere
    door = find_item('dvere', room['items'])

    if door is not None and door['state'] == 'zamknute':
        door['state'] = 'poliate'
        door['description'] = 'Dvere. Stále zamknuté, ale ako bonus sú poliate benzínom. ' \
                              'Je ti jasné, kto za to môže.'

        # a akcia
        print('Ta som odšroboval, rozohnal som sa a celý obsah kanistra som vylial na dvere. V '
              'miestnosti sa náhle rozľahol benzínový zápach. Proste vysoko-oktánová fajnotka.')
    else:
        print('Zahrkal som kanistrom a uistil som sa, že je stále plný.')


def use_matches(item, context):
    room = context['room']
    inventory = context['inventory']

    # musim byt v miestnosti s dverami, ktore su poliate benzinom!!!
    door = find_item('dvere', room['items'])
    if door and door['state'] == 'poliate':

        # zmazeme/vyhodime zapalky z hry (bud z miestnosti alebo z batohu)
        if item in room['items']:
            room['items'].remove(item)
        else:
            inventory.remove(item)

        # co sa stane s dverami:
        door['state'] = 'horiace'
        # zmena opisu
        door['description'] = 'Doteraz tie dvere iba voňali, teraz už aj horia. Zaujímavé, ' \
                              'čo všetko sa dnes deje v tom svete.'
        # nazov: horiace dvere
        door['name'] = 'horiace dvere'

        # akcia
        print(
            'Zahrkal si krabičkou zápaliek a jednu si z nej vytiahol. Nadýchol si sa, škrtol si a ona chytila. Usmial si sa a s úsmevom na tvári si horiacu zápalku voľne pohodil smerom k dverám. Tie neváhali a okamžite zbĺkli. Ten benzín urobil svoje.')
    else:
        print('Krabička zápaliek. Nič zaujímavé. Len na čo by som ich tak použil?')

    # todo: zapalky chytia az na tretikrat/posledna zapalka


def use_fire_extinguisher(item, context):
    room = context['room']

    # musia horiet dvere
    door = find_item('horiace dvere', room['items'])
    if door:
        # zmiznu dvere z miestnosti
        room['items'].remove(door)

        # hasiaci pristroj bude nepouzitelny
        item['features'].remove(features.USABLE)

        # zmenim mu opis na prazdny hasiaci pristroj
        item['description'] = 'Ručný hasiaci prístroj prázdny. Značka - červený.'

        # nastavim vychod z miestnosti
        room['exits']['west'] = 'garden'

        # akcia
        print(
            'Zahasil si dvere. Tie sa vplyvom tlaku hasiacej zmesy rozpadli a uvoľnili ti východ z miestnosti.')
    else:
        print('Aj by som nasnežil, ale nie je na čo.')
