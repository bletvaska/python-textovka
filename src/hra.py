#!/usr/bin/env python3
from world import world


def examine_item(line, inventory, room):
    """
    Examines given item

    Name of the item is given in the input line by the user. Then it is extracted and it is searched in inventory and
    room items. If the name of the item is not given, only short message is written back. If the name is given,
    then the item with this name is searched in inventory and room. If it is found, then it's description is written
    on the screen. If it is not found, error message is shown.

    :param line: input line from user
    :param inventory: players inventory
    :param room: current room
    """
    cmd = line.split(maxsplit=1)

    if len(cmd) == 1:
        print("Neviem čo chceš preskúmať.")
    else:
        print(f"preskumavam {cmd[1]}")

        for item in inventory + room["items"]:
            if cmd[1] == item["name"]:
                print(item["description"])
                break
        else:
            print("taky predmet tu nikde nevidim")


def show_inventory(inventory):
    """
    Prints content of the inventory on the screen
    :param inventory: player's inventory
    """
    if len(inventory) == 0:
        print("Batoh je prazdny.")
    else:
        items = []
        for item in inventory:
            items.append(item['name'])

        print("V batohu mas: " + ", ".join(items))


def show_room(room):
    print(f'Aktualne sa nachadzas v miestnosti {room["name"]}')
    print(room["description"])

    print("Mozne vychody:")
    for entry in room["exits"]:
        print(f"    {entry}")

    if len(room["items"]) != 0:
        # print("Vidíš: ")  # + ", ".join(room["items"]))
        # for item in room['items']:
        #     print(f"    {item['name']}")

        items = []
        for item in room['items']:
            items.append(item['name'])
        print("Vidíš: " + ", ".join(items))

    else:
        print("Nevidím tu nič zaujímavé.")


def take_item(line, inventory, room):
    cmd = line.split(maxsplit=1)

    if len(cmd) == 1:
        print("Neviem čo chceš zobrať.")
    else:
        name = cmd[1]
        for item in room["items"]:

            if name == item["name"]:
                if "movable" not in item['features']:
                    print('Tento predmet sa neda vziat')

                elif len(inventory) >= 2:
                    print('Batoh je plný.')

                else:
                    room['items'].remove(item)
                    inventory.append(item)
                    print(f'Do batohu si si vložil predmet {name}.')

                break
        else:
            print("taký predmet tu nikde nevidim.")


def drop_item(line, inventory, room):
    cmd = line.split(maxsplit=1)

    if len(cmd) == 1:
        print("Neviem čo chceš položiť.")
    else:
        name = cmd[1]
        for item in inventory:
            if name == item["name"]:
                inventory.remove(item)
                room['items'].append(item)
                print(f'Položil si predmet {name}.')
                break
        else:
            print("Taký predmet u seba nemáš.")


def use_spekacky(item, inventory, room):
    print('Pozivam spekacky')


def use_kluc(item, inventory, room):
    if room['name'] == 'l4':
        if 'chodba' not in room['exits']:
            print('Odomykám dvere z miestnosti.')
            room['exits'].append('chodba')
        else:
            print('Dvere sú už odomknuté.')
    else:
        print('V tejto miestnosti sa nenacházajú žiadne dvere, ktoré by si týmto kľúčikom otvoril.')


def use_kavomat(item, inventory, room):
    print('Kávomat sa zamyslel, nespokojne zahučal, zaškrípal a okamžite začal plniť svoju funkciu - začala z neho vytekať káva. Ešte teplá.')
    print('Po dokončení svojej práce sa kávomat rozhodol, že sa pokazí.')
    item['name'] = 'pokazeny kavomat'
    item['features'].remove('usable')
    cafe = {
        "name": "kava",
        "description": "Plastový pohárik plný teplej, práve načapovanej, kávy.",
        "features": ['movable', 'usable']
    }
    room['items'].append(cafe)


def use_pocitac(item, inventory, room):
    for item in room['items']:
        if item['name'] == 'instruktor':
            if item['happy'] == False:
                print('Tvoj najbľúbenejší inštruktor si všimol tvoj plíživý pohyb a prudko zareagoval. Čiernou fikskou si ťa poznačil nie len na čele aj v prezenčke. S tvojou kariérou čo by Python developer sa môžeš rozlúčiť. Ale môžeš to skúsiť nabudúce. Alebo na kofole')
            else:
                print('ta si to hackol')


def use_kava(item, inventory, room):
    if room['name'] != 'l4':
        print('Niet koho ponuknut.')
    else:
        for item in room['items']:
            if item['name'] == 'instruktor':
                item['happy'] = True
                print('ponukol si kavou instruktora. usmial sa. asi si jeho typ.')


def use_item(line, inventory, room):
    cmd = line.split(maxsplit=1)

    if len(cmd) == 1:
        print("Neviem čo chceš použiť.")
    else:
        name = cmd[1]

        for item in inventory + room['items']:
            if name == item['name']:
                if 'usable' in item['features']:
                    if name == 'spekacky':
                        use_spekacky(item, inventory, room)
                    elif name == 'kluc':
                        use_kluc(item, inventory, room)
                    elif name == 'kavomat':
                        use_kavomat(item, inventory, room)
                    elif name == 'pocitac':
                        use_pocitac(item, inventory, room)
                    elif name == 'kava':
                        use_kava(item, inventory, room)
                else:
                    print('Tento predmet sa neda pouzit')
                break
        else:
            print('Taky predmet tu nikde nevidim')


def play_game():
    inventory = [
        {
            "name": "zrkadielko",
            "description": "zrkadlo zrkadielko, povedz ze mi kto je najkrajsi v tejto firme?",
            "features": ["movable"]

        },
        {
            "name": "ponozky",
            "description": "Teple hrube ponozky idealne do letnych dni.",
            "features": ["movable"]
        }
    ]

    line = None
    location = "l4"
    show_room(world[location])

    while line != "koniec":
        line = input("tvoj prikaz > ")
        line = line.lower().strip()

        if line in world:
            if line in world[location]["exits"]:
                location = line
                show_room(world[location])
            else:
                print("Tam sa neda ist.")

        elif line == "o hre":
            print(
                "Tuto mocnu hru naprogramoval mocny programator mire(c) v roku 2018. mozes ho podporit svojim vsimnym na ucte IBAN SK123456789.")

        elif line == "koniec":
            print(
                "no co uz s tebou, ked si sa rozhodol to trapenie ukoncit. ale diky ze si sa stavil. nezabudni na bankovy prevod.")

        elif line == "rozhliadni sa":
            show_room(world[location])

        elif line == "inventar":
            show_inventory(inventory)

        elif line.startswith("preskumaj"):
            examine_item(line, inventory, world[location])

        elif line.startswith("vezmi"):
            take_item(line, inventory, world[location])

        elif line.startswith("poloz"):
            drop_item(line, inventory, world[location])

        elif line.startswith("pouzi"):
            use_item(line, inventory, world[location])

        else:
            print("tam sa neda ist")


if __name__ == '__main__':
    play_game()
