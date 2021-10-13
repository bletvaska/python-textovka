from utils import get_item_by_name
from features import USABLE


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