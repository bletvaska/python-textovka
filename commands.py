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

    def exec(self, context: Context):
        print(
            "Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou."
        )
        print("Túto hru spáchal v 2022 (c) mirek.")


@dataclass(frozen=True)
class LookAround:
    name: str = "rozhliadni sa"
    description: str = "Vypise popis miestnosti, kde sa prave nachadzas."

    def exec(self, context: Context):
        show_room(context.room)


@dataclass(frozen=True)
class Quit:
    name: str = "koniec"
    description: str = "ukončí rozohratú hru"

    def exec(self, context: Context):
        line = input("Naozaj chceš skončiť? (a/n) ").lower().lstrip().rstrip()
        if line == "a":
            context.state = states.QUIT


commands = [About(), LookAround(), Quit()]


def cmd_about(context: Context, line: str):
    print(
        "Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou."
    )
    print("Túto hru spáchal v 2022 (c) mirek.")


def cmd_commands(context: Context, line: str):
    print("Zoznam dostupných príkazov:")
    print("  * inventar - vypíše obsah batohu")
    print("  * koniec - ukončí rozohratú hru")
    print("  * o hre - zobrazí informácie o hre")
    print("  * poloz - vylozi predmet z batohu do aktuálnej miestnosti")
    print("  * preskumaj - zobrazí opis zvoleného predmetu")
    print("  * prikazy - zobrazí zoznam príkazov hry")
    print("  * rozhliadni sa - Vypise popis miestnosti, kde sa prave nachadzas.")
    print("  * vezmi - vezme predmet a miestnosti a vloží si ho do batohu")


def cmd_inventory(context: Context, line: str):
    if context.backpack == []:
        print("Batoh je prázdny.")
    else:
        print("V batohu máš:")
        for item in context.backpack:
            print(f" * {item['name']}")


def cmd_take(context: Context, line: str):
    name = line.split(sep="vezmi")[1].lstrip()

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


def cmd_examine(context: Context, line: str):
    name = line.split(sep="preskumaj")[1].lstrip()

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


def cmd_drop(context: Context, line: str):
    name = line.split(sep="poloz")[1].lstrip()

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


def cmd_quit(context: Context, line: str):
    line = input("Naozaj chceš skončiť? (a/n) ").lower().lstrip().rstrip()
    if line == "a":
        context.state = states.QUIT
