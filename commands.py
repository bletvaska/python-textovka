from dataclasses import dataclass, field
from typing import List
from helpers import get_item_by_name, show_room
from items.features import MOVABLE
from models import Context
import states


# command = {"description": str, "aliases": list, "name": str, "exec": function}


# @dataclass
# class Command:
#     description: str
#     aliases: list
#     name: str

#     def exec():
#         pass


@dataclass(frozen=True)
class About:
    name: str = "o hre"
    description: str = "zobrazí informácie o hre"

    def exec(self, context: Context, name: str):
        print(
            "Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou."
        )
        print("Túto hru spáchal v 2022 (c) mirek.")


@dataclass(frozen=True)
class LookAround:
    name: str = "rozhliadni sa"
    description: str = "Vypise popis miestnosti, kde sa prave nachadzas."

    def exec(self, context: Context, name: str):
        show_room(context.room)


@dataclass(frozen=True)
class Quit:
    name: str = "koniec"
    description: str = "ukončí rozohratú hru"

    def exec(self, context: Context, name: str):
        line = input("Naozaj chceš skončiť? (a/n) ").lower().lstrip().rstrip()
        if line == "a":
            context.state = states.QUIT


@dataclass(frozen=True)
class ListOfCommands:
    name: str = "prikazy"
    description: str = "vypíše zoznam príkazov"

    def exec(self, context: Context, name: str):
        print("Zoznam dostupných príkazov:")

        for command in list_of_commands:
            print(f"  * {command.name} - {command.description}")


@dataclass(frozen=True)
class Inventory:
    name: str = "inventar"
    description: str = "vypíše obsah batohu"

    def exec(self, context: Context, name: str):
        if context.backpack == []:
            print("Batoh je prázdny.")
        else:
            print("V batohu máš:")
            for item in context.backpack:
                print(f" * {item['name']}")


@dataclass(frozen=True)
class TakeItem:
    name: str = "vezmi"
    description: str = "vezme predmet z miestnosti a vloží si ho do batohu"

    def exec(self, context: Context, name: str):
        # if no item was given, then quit
        if len(name) == 0:
            print("Neviem, aký predmet chceš vziať.")
            return

        item = get_item_by_name(name, context.room["items"])

        # if item was not found, then quit
        if item is None:
            print("Taký predmet tu nikde nevidím.")
            return

        # if item is now movable, then quit
        if MOVABLE not in item["features"]:
            print("Tento predmet sa nedá zobrať.")
            return

        # action
        context.room["items"].remove(item)
        context.backpack.append(item)
        print(f"Do batohu si vložil predmet {name}.")


@dataclass(frozen=True)
class ExamineItem:
    name: str = "preskumaj"
    description: str = "vypíše opis daného predmetu"

    def exec(self, context: Context, name: str):
        # if no item was given, then quit
        if len(name) == 0:
            print("Neviem, čo chceš preskúmať.")
            return

        item = get_item_by_name(name, context.backpack + context.room["items"])

        # if item was not found, then quit
        if item is None:
            print("Tento predmet tu nikde nevidím.")
            return

        # action
        print(item["description"])


@dataclass(frozen=True)
class DropItem:
    name: str = "poloz"
    description: str = "vyloží predmet z batohu do miestnosti"

    def exec(self, context: Context, name: str):
        # if no item was given, then quit
        if len(name) == 0:
            print("Neviem, aký predmet chceš položiť.")
            return

        # find item by name
        item = get_item_by_name(name, context.backpack)

        # if no item found, then quit
        if item is None:
            print("Taký predmet pri sebe nemáš.")
            return

        # poloz ho do miestnosti
        context.room["items"].append(item)

        # zmaz ho z batohu
        context.backpack.remove(item)

        # render
        print(f"Do miestnosti si vyložil predmet {name}.")


list_of_commands = [
    About(),
    LookAround(),
    Quit(),
    Inventory(),
    TakeItem(),
    ExamineItem(),
    DropItem(),
    ListOfCommands(),
]
