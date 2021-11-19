import json


def _exec(context: dict, filename: str):
    # check if filename was given
    if filename == '':
        print('Chyba: Názov súboru pre uloženie histórie nebol zadaný.')
        return

    # save
    try:
        with open(filename, 'w+') as file:
            json.dump(context['history'], file)
            print('Súbor bol úspešne uložený.')
    except PermissionError as ex:
        print('Chyba: Nemáte dostatočné oprávnenie pre uloženie súboru na dané miesto.')
    except IsADirectoryError as ex:
        print('Chyba: Pokúšate sa uložiť súbor s názvom existujúceho priečinku.')
    except Exception as ex:
        print('Chyba: Súbor sa nepodarilo uložiť.')
        print(ex)


cmd = {
    'name': "uloz",
    'description': 'uloží aktuálny stav hry do súboru',
    'aliases': ("save",),
    'exec': _exec,
}
