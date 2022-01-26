from helpers import get_item_by_name
from items.features import MOVABLE
import states


def cmd_about():
    print(
        "Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou."
    )
    print("Túto hru spáchal v 2022 (c) mirek.")


def cmd_commands():
    print("Zoznam dostupných príkazov:")
    print("  * inventar - vypíše obsah batohu")
    print("  * koniec - ukončí rozohratú hru")
    print("  * o hre - zobrazí informácie o hre")
    print("  * poloz - vylozi predmet z batohu do aktuálnej miestnosti")
    print("  * preskumaj - zobrazí opis zvoleného predmetu")
    print("  * prikazy - zobrazí zoznam príkazov hry")
    print("  * rozhliadni sa - Vypise popis miestnosti, kde sa prave nachadzas.")
    print("  * vezmi - vezme predmet a miestnosti a vloží si ho do batohu")


def cmd_inventory(backpack: list):
    if backpack == []:
        print("Batoh je prázdny.")
    else:
        print("V batohu máš:")
        for item in backpack:
            print(f" * {item['name']}")


def cmd_take(room, backpack, line):
    name = line.split(sep="vezmi")[1].lstrip()

    # if no item was given, then quit
    if len(name) == 0:
        print("Neviem, aký predmet chceš vziať.")
        return

    item = get_item_by_name(name, room["items"])

    # if item was not found, then quit
    if item is None:
        print("Taký predmet tu nikde nevidím.")
        return

    # if item is now movable, then quit
    if MOVABLE not in item["features"]:
        print("Tento predmet sa nedá zobrať.")
        return

    # action
    room["items"].remove(item)
    backpack.append(item)
    print(f"Do batohu si vložil predmet {name}.")


def cmd_examine(room, backpack, line):
    name = line.split(sep="preskumaj")[1].lstrip()

    # if no item was given, then quit
    if len(name) == 0:
        print("Neviem, čo chceš preskúmať.")
        return

    item = get_item_by_name(name, backpack + room["items"])

    # if item was not found, then quit
    if item is None:
        print("Tento predmet tu nikde nevidím.")
        return

    # action
    print(item["description"])


def cmd_drop(room: dict, backpack, line):
    name = line.split(sep="poloz")[1].lstrip()

    # if no item was given, then quit
    if len(name) == 0:
        print("Neviem, aký predmet chceš položiť.")
        return

    # find item by name
    item = get_item_by_name(name, backpack)

    # if no item found, then quit
    if item is None:
        print("Taký predmet pri sebe nemáš.")
        return

    # poloz ho do miestnosti
    room["items"].append(item)

    # zmaz ho z batohu
    backpack.remove(item)

    # render
    print(f"Do miestnosti si vyložil predmet {name}.")


def cmd_quit(game_state: str):
    line = input("Naozaj chceš skončiť? (a/n) ").lower().lstrip().rstrip()
    if line == "a":
        return states.QUIT
    else:
        return game_state
