#!/usr/bin/env python3

# standardne moduly
import json

# tretostranove moduly
from typing import List

import requests

# moje moduly
import states
from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.drop import Drop
from commands.east import East
from commands.explore import Explore
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.north import North
from commands.quit import Quit
from commands.save import Save
from commands.south import South
from commands.take import Take
from commands.use import Use
from commands.west import West
from context import Context

from items.newspaper import Newspaper
from utils import get_room_by_name
import config
from world import world


def parse(line: str, commands: List[Command]) -> tuple:
    for cmd in commands:
        aliases = [cmd.name] + cmd.aliases

        for alias in aliases:
            if line.startswith(alias):
                arg = line.removeprefix(alias).strip()
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
    # world = _get_world_from_parse('SgojO2UAvw')

    # create context
    context = Context(
        backpack={
            'items': [
                Newspaper()
            ],
            'capacity': 2
        },
        room=get_room_by_name('dungeon', world),
        world=world,
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
    context.room.show()

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
        if context.room.name == 'garden':
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
