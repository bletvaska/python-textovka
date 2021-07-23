from helper import get_item_by_name
import random


def use_item(context: dict, name: str):
    if name == 'noviny':
        use_newspaper(context)
    elif name == 'kanister':
        use_canister(context)
    elif name == 'zapalky':
        use_matches(context)
    elif name == 'vedro':
        use_bucket(context)


def use_bucket(context: dict):
    room = context['room']
    backpack = context['backpack']

    # prerequisities
    # 1. v miestnosti su horiace dvere
    door = get_item_by_name(room['items'], 'horiace dvere')
    if door is None:
        print('Aj by som dačo popolieval, ale neni čo. Ani smädný nie som. Tak to nechám na neskôr.')
        return

    # action
    # 1. vedro sa stane prazdnym (zostane na mieste, len sa zmeni jeho opis) a nepoužiteľným
    bucket = get_item_by_name(room['items'] + backpack['items'], 'vedro')
    bucket['description'] = 'Prázdne vedro.'
    bucket['features'].remove('usable')

    # 2. dvere zmiznu z miestnosti
    room['items'].remove(door)

    # 3. objavi vychod z miestnosti - na sever
    room['exits']['north'] = 'hall'

    # render
    print('Ta si sa rozohnal a celý obsah vedra si vylial na horiace dvere. Ten žiariaci plameň sa ti podarilo zahasiť a dvere sa pod tlakom rozpadli. Vyzerá to tak, že východ z tvojho väzenia je voľný.')


def use_matches(context: dict):
    room = context['room']
    backpack = context['backpack']

    # prerequisities
    door = get_item_by_name(room['items'], 'dvere poliate benzinom')
    if door is None:
        print('Aj by som dačo zapálil, ale zapáliť celú krabičku len tak... Tomu sa hovorí plytvanie.')
        return

    matches = get_item_by_name(room['items'] + backpack['items'], 'zapalky')
    if matches['attempts'] > 0:
        matches['attempts'] -= 1

        if matches['attempts'] == 2:
            print('Vytiahol si jednu zápalku z krabičky, škrtol si a sa zlomila. Do mače, povedal si si pre seba. Už mi zostávajú len dve zápalky.')
            return

        elif matches['attempts'] == 1:
            print('Vytiahol si druhú zápalku z krabičky, nadýchol si sa a škrtol si. Objavil sa plameň. Usmial si sa. A plameň zmizol. Zosmutnel si. Už mi zostáva len posledná zápalaka.')
            return

        else:
            print(
                'Z krabičky si vytiahol poslednú zápalku. Nuž čo - do tretice šecko dobre. A škrtol si.')

    # action
    # door on fire
    door['name'] = 'horiace dvere'
    door['description'] = 'Dvere s mohutným plameňom. Ten zrejme nebol súčasťou objednávky. Ani priblížiť, čo také teplo z nich sála'

    # remove matches

    if matches in room['items']:
        room['items'].remove(matches)
    else:
        backpack['items'].remove(matches)

    # render scene
    print('Priložil si ju k dverám, ktoré okamžite vzbĺkli. Neviem, či to bolo súčasťou tvojho zámeru, ale výsledok je teda mocný.')


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

    # render scene
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
