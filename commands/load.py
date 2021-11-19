import json


def _exec(context: dict, filename: str):
    # check if filename was given
    if filename == '':
        print('Chyba: Názov súboru pre načítanie hry nebol zadaný.')
        return

    # save
    try:
        with open(filename, 'r+') as file:
            # load history
            history = json.load(file)
            print(history)

            # init game
            # context

    except PermissionError as ex:
        print('Chyba: Nemáte dostatočné oprávnenie pre načítanie súboru z daného miesto.')
    except IsADirectoryError as ex:
        print('Chyba: Pokúšate sa načítať súbor s názvom existujúceho priečinku.')
    except Exception as ex:
        print('Chyba: Súbor sa nepodarilo načítať.')
        print(ex)


cmd = {
    'name': "nacitaj",
    'description': 'načíta uložený stav hry',
    'aliases': ("load", "nahraj"),
    'exec': _exec,
}
