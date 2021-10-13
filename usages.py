from utils import get_item_by_name
from features import USABLE


def use_bucket(context, bucket):
    # init

    # scenario
    # 1. aktualizujeme vedro
    #    - je prazdne
    #    - nebude pouzitelne
    # 2. zmazem dvere z miestnosti/hry
    # 3. ???
    # 4. rendering - ta si uhasil dvere a sa rozpadli


def use_matches(context, matches):
    # init
    room = context['room']
    backpack = context['backpack']['items']

    # 1. overim, ci su dvere poliate benzinom
    #    - ci su dvere v stave 'wet'
    door = get_item_by_name('dvere', room['items'])
    if door['state'] != 'wet':
        print('Zahrkal si krabičkou pri ušku, aby si sa uistil, že nie je prázdna. Usmial si sa.')
        return

    # 2. aktualizujem zapalky
    #    - odstranim ich z hry
    if matches in room['items']:
        room['items'].remove(matches)
    else:
        backpack.remove(matches)

    # 3. aktualizujem dvere
    #    - zmenim description - dvere v plamenoch
    #    - zmenim stav na 'on fire'
    door['description'] = 'Dvere v plameňoch.'
    door['state'] = 'on fire'
    door['name'] = 'horiace dvere'

    # 4. renderujem scenu - skrtol si zapalkou a dvere zacali horiet
    print(
        'Otvoril si krabičku a vytiahol si z nej jedinú zápalku. Nadýchol si sa a škrtol si. Miestnosť sa okamžite rozžiarila. Síce nie tvojim šarmantným úsmevom, ale plamenňom, ktorý oakmžite zachvátil dvere nasiaknuté vysokooktánovým benzínom. Nejedno srdce pyromana by teraz vzplanulo radosťou.')


def use_canister(context, canister):
    # init
    room = context['room']

    # 1. aktualizujem dvere:
    #    - description dvere su poliate benzinom
    door = get_item_by_name('dvere', room['items'])
    door['description'] = 'Masívne dubové dvere dôkladne nasiaknuté vysokooktánovým benzínom.'
    door['state'] = 'wet'

    # 2. aktualizujem kanister
    #    - description - prazdny kanister
    #    - features - nebude USABLE
    canister['name'] = 'prazdny kanister'
    canister['description'] = 'Prázdny kanister od benzínu.'
    canister['features'].remove(USABLE)

    # 3. render - vylejem kanister na dvere
    print(
        'Odšroboval si zátku kanistra a celý jeho obsah si vylial na dvere. Veľmi dôkladne si ich pooblieval a v miestnosti sa rozľahla vôňa vysokooktánového benzínu. Srdce nejedného feťáka by v tejto chvíli zaplesalo Blahom.')
