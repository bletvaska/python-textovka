#!/usr/bin/env python3
"""
Textovka

Mocna to hra textoveho charakteru. Naprogramovana v priestoroch fa
GlobalLogic v Kosicoch. Mocne to je.
Autor: mirek (c) 2018
"""
from world import world


def examine_item(room, inventory, line):
    """
    Shows item description

    This function shows description of the item specified by the player
    on command line. If the item is not specified (only the command EXAMINE
    is entered), then error message is shown. If the item is specified and
    the item is located in room or in inventory, then it's description is
    printed on the screen. If the given item is not found in the room or
    inventory, then error message is shown.
    :param room: current room
    :param inventory: players inventory (list of items)
    :param line: command line (user's input)
    """
    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print("Ta ja neznám čo chceš skúmať.")
    else:
        for item in inventory + room["items"]:
            if item['name'] == cmd[1]:
                print(item['description'])
                break
        else:
            print("Taký predmet tu nikde nevidím.")


def show_room(room):
    """
    Describes room

    This function prints on the screen the description of the room, with
    all of it's (visible) exits and (visible) items, which are located there.
    :param room: the room reference (as dictionary)
    """
    print(f"Miestnost: {room['name']}")
    print(room["description"])
    print("Možné východy:")
    for entry in room['exits']:
        print(f"    {entry}")

    # if len(room["items"]) == 0:
    if not room["items"]:
        print("Nevidíš tu nič zaujímavé.")
    else:
        items = []
        for item in room['items']:
            items.append(item['name'])
        print("Vidíš: " + ', '.join(items))


def show_inventory(inventory):
    """
    Shows player inventory

    :param inventory: player inventory (as a list)
    """
    if len(inventory) == 0:
        print("Batoh je prazdny.")
    else:
        items = []
        for item in inventory:
            items.append(item['name'])
        print("V batohu mas: " + ', '.join(items))


def take_item(room, inventory, line, history):
    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print("Ta ja neznám čo chceš zobrať.")
    else:
        name = cmd[1]
        for item in room["items"]:
            if item['name'] == name:
                if 'movable' not in item['features']:
                    print('Tento predmet sa nedá vziať.')

                elif len(inventory) == 3:
                    print('Batoh je plný.')

                else:
                    room['items'].remove(item)
                    inventory.append(item)
                    print(f'Z miestnosti si vzal predmet {name}.')
                    history.append(line)

                break
        else:
            print("Taký predmet tu nikde nevidím.")


def drop_item(room, inventory, line, history):
    cmd = line.split(maxsplit=1)
    if len(cmd) == 1:
        print("Ta ja neznám čo chceš položiť.")
    else:
        name = cmd[1]
        for item in inventory:
            if item['name'] == name:
                inventory.remove(item)
                room['items'].append(item)
                print(f'Položil si predmet {name}.')
                history.append(line)
                break
        else:
            print("Taký predmet u seba nemáš.")


def use_kluc(item, inventory, room):
    if room['name'] == 'garaz':
        if 'schodisko' not in room['exits']:
            print('Odomykám dvere z miestnosti.')
            room['exits'].append('schodisko')
        else:
            print('Dvere sú už odomknuté.')
    else:
        print('V tejto miestnosti sa nenacházajú žiadne dvere, ktoré by si týmto kľúčikom otvoril.')


def use_kavomat(item, inventory, room):
    print("Automat zahrkal, zarachotil a chopil sa svojej práce - začal tankovať kávu. Teplú.")
    cafe = {
        "name": "kava",
        "description": "Šialok teplej hustej tmavej sladkej, jedným slovom odpornej, kávy.",
        "features": ['movable', 'usable']
    }
    room['items'].append(cafe)

    print('Nahle sa kavomat rozhodol, ze sa pokazi. A sa pokazil.')
    item['name'] = 'pokazeny kavomat'
    item['features'].remove('usable')


def use_ovladac(item, inventory, room):
    for item in room['items']:
        if item['name'] == 'ochrankar':
            if item['has cafe'] == False:
                print('Zial, neusiel si pozornosti bystreho srsiaceho zraku zavaliteho ochrankara ukrajinskeho typu. Hmm... zrejme kvoli tejto vlastnosti zastava tuto mocnu poziciu. Co pre teba nie je velmi dobre. Si nikam nepostupil. Si tu skoncil. Sorry.')
            else:
                print('Ochrankár na teba žmurkol, keď sa za tebou zatvárali dvere výťahu. Najvyššie poschodie v tejto spoločnosti znamená dlhý a bezstarostný život. Vydal si sa k výšinám svojej úspešnej budúcnsti. Live long and prosper, player one.')


def use_kava(item, inventory, room):
    if room['name'] == 'vytah':
        print('Ponukol si kavu nenavistou srsiacemu ochrankari ukrajinskeho typu. Srkol dusok a usmial sa na teba. Jeho chladne srdce sa prave roztopilo...')

        # give cafe to ochrankar
        for ochrankar in room['items']:
            if ochrankar['name'] == 'ochrankar':
                ochrankar['has cafe'] = True

        # remove cafe from game
        if item in inventory:
            inventory.remove(item)
        else:
            room['items'].remove(item)
    else:
        print('Tak neni koho ponuknut touto kavou.')


def use_item(room, inventory, line, history):
    cmd = line.split(maxsplit=1)

    if len(cmd) == 1:
        print("Neviem čo chceš použiť.")
    else:
        name = cmd[1]

        for item in inventory + room['items']:
            if name == item['name']:
                if 'usable' in item['features']:
                    if name == 'kluc':
                        use_kluc(item, inventory, room)
                    elif name == "kavomat":
                        use_kavomat(item, inventory, room)
                    elif name == 'ovladac':
                        use_ovladac(item, inventory, room)
                    elif name == 'kava':
                        use_kava(item, inventory, room)
                    history.append(line)
                else:
                    print('Tento predmet sa neda pouzit')
                break
        else:
            print('Taky predmet tu nikde nevidim')


def save_history(line, history):
    try:
        f = open('history.csv', 'w')

        for entry in history:
            f.write(f'{entry}\n')

        f.close()

        print('Historia bola uspesne ulozena.')
    except PermissionError:
        print('Chyba: Nemas dostatocne prava na ulozenie suboru.')
    except FileNotFoundError:
        print('Chyba: Uvedena cesta k suboru neexistuje.')
    except Exception:
        print('Chyba: Subor sa nepodarilo ulozit.')


def play_game():
    """
    Game loop

    This function starts the game. This is the main game loop.
    """
    inventory = [
        {
            "name": 'domaca',
            "description": "Fajná pálená domáca.",
            "features": ["movable"]
        },
        {
            "name": "slanina",
            "description": "Riadna niekoľkovrstvová adidska.",
            "features": ["movable"]
        },
        {
            "name": "korcula",
            "description": "Taká ostrá, že by sa s ňou dalo aj oholiť.",
            "features": ["movable"]
        }
    ]
    location = "garaz"
    show_room(world[location])
    line = None
    history = []

    while line != "koniec":
        line = input("> ")
        line = line.strip().lower()

        if line in world:
            if line in world[location]["exits"]:
                location = line
                show_room(world[location])
                history.append(line)
            else:
                print("Tam sa neda ist")

        elif line == "o hre":
            print(
                "Tuto mocnu hru vytvoril mocny mire(c) 2018. Mozes jeho mocnu tvorbu podporit svojim mocnym prispevkom na ucet s IBAN-om SK2341324123487. diky")

        elif line == "koniec":
            print("Dakujem ti, ze si sa zahral tuto mocnu nedokoncenu hru. Nezabudni na svoj prispevok. Diky.")

        elif line == "rozhliadni sa":
            show_room(world[location])

        elif line == "inventar":
            show_inventory(inventory)

        elif line.startswith("preskumaj"):
            examine_item(world[location], inventory, line)

        elif line.startswith("vezmi"):
            take_item(world[location], inventory, line, history)

        elif line.startswith("poloz"):
            drop_item(world[location], inventory, line, history)

        elif line.startswith("pouzi"):
            use_item(world[location], inventory, line, history)

        elif line.startswith("uloz"):
            save_history(line, history)

        else:
            print("taky prikaz nepoznam")


if __name__ == '__main__':
    play_game()
