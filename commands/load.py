import json

from game import init_game
from helpers import show_room


def _parse(line: str, context: dict) -> tuple:
    for cmd in context['commands']:
        for alias in cmd['aliases'] + (cmd['name'],):
            if line.startswith(alias):
                param = line.split(alias)[1].strip()
                return cmd, param

    return (None, None)


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
            context2 = init_game()
            context['world'] = context2['world']
            context['backpack']['items'] = context2['backpack']['items']
            context['room'] = context2['room']

            # interpret commands
            for cmd in history:
                command, param = _parse(cmd, context)
                callback = command['exec']
                callback(context, param)

            # show room
            show_room(context['room'])
            print('Pozícia bola úspešne načítaná.')

    except PermissionError as ex:
        print('Chyba: Nemáte dostatočné oprávnenie pre načítanie súboru z daného miesto.')
    except IsADirectoryError as ex:
        print('Chyba: Pokúšate sa načítať súbor s názvom existujúceho priečinku.')
    # except Exception as ex:
    #     print('Chyba: Súbor sa nepodarilo načítať.')
    #     print(ex)


cmd = {
    'name': "nacitaj",
    'description': 'načíta uložený stav hry',
    'aliases': ("load", "nahraj"),
    'exec': _exec,
}
