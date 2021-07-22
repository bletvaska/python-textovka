from helper import get_item_by_name
import random


def use_item(context: dict, name: str):
    if name == 'noviny':
        use_newspaper(context)
    elif name == 'kanister':
        use_canister(context)


def use_canister(context: dict):
    room = context['room']
    backpack = context['backpack']

    # prerequisities
    door = get_item_by_name(room['items'], 'dvere')
    if door is None:
        print('Ta neviem, čo by som s tým benzínom v kanistri tu porobil. Ani zapáliť neni čo drevené.')
        return

    # action
    canister = get_item_by_name(room['items'] + backpack['items'], 'kanister')
    canister['description'] = 'Prázdny kanister. Vôňa benzínu sa rinie z jeho útrob.'
    canister['features'].remove('usable')

    door['name'] = 'dvere poliate benzinom'
    door['description'] = 'Veľké masívne dubové dvere čerstvo nasiaknuté čerstvým benzínom. 99 oktánovým. Kvalitka.'

    # the scene
    print('Odšroboval si kanister, privoňal si k obsahu a zhodnotil si - benzín, ešte čerstvý. Neváhal si a polial si dôkladne celým jeho obsahom veľké masívne dvere. Ani kvapka benzínu nevyšla nazmar.')


def use_newspaper(context: dict):
    headlines = [
        'Nezaočkovaný lekár a po ňom aj športovci. V českom olympijskom tíme sa šíri covid',
        'Keď som videl počet mŕtvych, zabudol som dýchať. Slovenský autobusár v Nórsku Ondrej Sokol spomína na 22. júl',
        'Sledovaný novinár z Maďarska: Chceli byť krok predo mnou, úplne som prišiel o súkromie',
        'Prežil Breivikovo vraždenie: Vyslovujme jeho meno, inak z neho spravíme Voldemorta',
        'Prečo si nevybrali veľkú hviezdu a prečo práve Seattle? Všetko o novom klube NHL'
    ]

    print('Zalistoval si v novinách a tvoj zrak upútal tento nadpis:')
    print(random.choice(headlines))
    print('Husté, si si povedal popod fúz...')
