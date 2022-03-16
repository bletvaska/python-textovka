#!/usr/bin/env python3

# standardne moduly
import json

# tretostranove moduly
import requests

# moje moduly
import states
from commands import About, Commands, Drop, Explore, Inventory, LookAround, Quit, Save, Take, Use, South, North, East, \
    West
from context import Context

from features import MOVABLE, USABLE
# from world import world
from utils import get_room_by_name, show_room
import config


def parse(line: str, commands: list) -> dict:
    for cmd in commands:
        if line.startswith(cmd.name):
            arg = line.removeprefix(cmd.name).strip()
            return (cmd, arg)

    return (None, None)


def _post_world_to_parse(world: dict):
    payload = {
        "world": world,
        "backpack": [],
        "start_room": ''
    }

    # TODO: not secure
    headers = {
        'X-Parse-Application-Id': config.app_id,
        'X-Parse-REST-API-Key': config.rest_api_key,
        'Content-Type': 'application/json'
    }

    with requests.post(f'{config.base_url}/worlds', headers=headers, json=payload) as response:
        print(response.status_code)
        print(response.json())


def _load_world_from_file():
    # load the world
    try:
        with open('world.ascii.json', 'r') as file:
            world = json.load(file)

    except FileNotFoundError as ex:
        print('CHYBA: Súbor so svetom "world.json" sa nenašiel. Hra sa preto nedá spustiť a bude ukončená.')
        quit(1)

    except PermissionError as ex:
        print("CHYBA: Prístup odopretý.")
        quit(1)

    except Exception as ex:
        print('CHYBA: Neznáma chyba.')
        print(f'CHYBA: {ex}')
        quit(1)

    return world


def _save_world_to_file(world: dict):
    # save the world
    file = open('world.json', 'w')
    json.dump(world, file, ensure_ascii=False, indent=4)
    file.close()


def _get_world_from_parse(object_id: str) -> dict:
    headers = {
        'X-Parse-Application-Id': config.app_id,
        'X-Parse-REST-API-Key': config.rest_api_key,
    }

    with requests.get(f'{config.base_url}/worlds/{object_id}', headers=headers) as response:
        if response.status_code != 200:
            print('CHYBA: Chyba pri sťahovaní mapy z internetu.')
            print(response.json())
            quit(2)

        data = response.json()
        return data['world']


def play_game():
    # init game
    # load world from file
    # world = _load_world_from_file()

    # download world from parse.com
    world = _get_world_from_parse('SgojO2UAvw')

    # create context
    context = Context(
        backpack={
            'items': [
                {
                    'name': 'noviny',
                    'description': 'dennik sme s autorskou strankou sama marca',
                    'features': [MOVABLE, USABLE],
                }
            ],
            'capacity': 2
        },
        room=get_room_by_name('dungeon', world),
        world=world,
        history=[],
        commands=[
            About(),
            Commands(),
            Drop(),
            East(),
            Explore(),
            Inventory(),
            LookAround(),
            North(),
            Quit(),
            Save(),
            South(),
            Take(),
            Use(),
            West(),
        ]
    )

    # game intro
    print('Indiana Jones')
    print('alebo veľké Pythoňácke dobrodružstvo')
    show_room(context.room)

    # game loop
    while context.state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        # empty input?
        if len(line) == 0:  # line == ''
            continue

        # parse
        (cmd, arg) = parse(line, context.commands)
        if cmd is None:
            print('Tento príkaz nepoznám.')
        else:
            cmd.exec(context, arg)

        # check room name
        if context.room['name'] == 'garden':
            print("__        __   _ _   ____                   _ ")
            print("\\ \\      / /__| | | |  _ \\  ___  _ __   ___| |")
            print(" \\ \\ /\\ / / _ \\ | | | | | |/ _ \\| '_ \\ / _ \\ |")
            print("  \\ V  V /  __/ | | | |_| | (_) | | | |  __/_|")
            print("   \\_/\\_/ \\___|_|_| |____/ \\___/|_| |_|\\___(_)")
            print()

            context.state = states.WIN

    print('(c) 2021-2022 spáchal mirek ako výsledný projekt hustého akvaristicko-teraristického školenia')


if __name__ == '__main__':
    play_game()
