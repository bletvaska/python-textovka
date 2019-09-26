def show_room(room: dict):
    # show description
    print(room['description'])

    # show exits
    if len(room['exits']) > 0:
        print('Možné východy:')
        for exit in room['exits']:
            print(f"    {exit}")
    else:
        print('Z miestnosti nevedú žiadne východy.')

    # show items
    if len(room['items']) > 0:
        print('Vidíš:')
        for item in room['items']:
            print(f'     {item["name"]}')
    else:
        print('Nevidíš nič zvláštne.')


class Command:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def exec(self, current_room:str, world:dict, backpack:list):
        pass


class About(Command):
    def __init__(self):
        super().__init__('o hre', 'Túto hru spáchal mirek v roku 2019. Celkom fajnú.')

    def exec(self, current_room, world, backpack):
        print(self._description)


class LookAround(Command):
    def __init__(self):
        super().__init__('rozhliadni sa', 'Vypíše opis miestnosti.')

    def exec(self, current_room, world, backpack):
        show_room(world[current_room])


class Inventory(Command):
    def __init__(self):
        super().__init__('inventar', 'Zobrazí obsah batohu.')

    def exec(self, current_room, world, backpack):
        if len(backpack) > 0:
            print('V batohu máš:')
            for item in backpack:
                print(f'     {item["name"]}')
        else:
            print('Batoh je prázdny.')


class Help(Command):
    def __init__(self):
        super().__init__('pomoc', 'Zobrazí pomocníka k jednotlivým príkazom')

    def exec(self, current_room, world, backpack):
        print('ta pomoz si sam.')


class Commands(Command):
    def __init__(self):
        super().__init__('prikazy', 'Zobrazí zoznam príkazov.')

    def exec(self, current_room, world, backpack):
        cmds = (
            'rozhliadni sa',
            'o hre',
            'pomoc',
            'prikazy',
            'sever',
            'juh',
            'vychod',
            'zapad',
            'dolu',
            'vezmi',
            'poloz',
            'preskumaj',
            'koniec'
        )
        print('\n'.join(cmds))


class Commands(Command):
    def __init__(self):
        super().__init__('koniec', 'Ukončí hru.')

    def exec(self, current_room, world, backpack):
        print('ta diky ze si si zahral tuto mocnu hru, lebo je fakt mocna.')


class East(Command):
    def __init__(self):
        super().__init__("vychod", "Presunie sa na vychod.")

    def exec(self, current_room:str, world:dict, backpack:list):
        """
        Enter the room on east from current room.
        If there is no exit to the east, then no change. The new room will be returned from the function.
        :param world: the world the player is in
        :param current_room: the name of current room player is in
        :return: the name of new room on the east
        """
        room = world[current_room]

        if 'vychod' in room['exits']:
            current_room = room['exits']['vychod']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

        return current_room


class West(Command):
    def __init__(self):
        super().__init__("zapad", "Presunie sa na západ.")

    def exec(self, current_room:str, world:dict, backpack:list):
        room = world[current_room]

        if 'zapad' in room['exits']:
            current_room = room['exits']['zapad']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

        return current_room


class North(Command):
    def __init__(self):
        super().__init__("sever", "Presunie sa na sever.")

    def exec(self, current_room:str, world:dict, backpack:list):
        room = world[current_room]

        if 'sever' in room['exits']:
            current_room = room['exits']['sever']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

        return current_room


class South(Command):
    def __init__(self):
        super().__init__("juh", "Presunie sa na juh.")

    def exec(self, current_room:str, world:dict, backpack:list):
        room = world[current_room]

        if 'juh' in room['exits']:
            current_room = room['exits']['juh']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

        return current_room


class Down(Command):
    def __init__(self):
        super().__init__("dolu", "Presunie sa dolu.")

    def exec(self, current_room:str, world:dict, backpack:list):
        room = world[current_room]

        if 'dolu' in room['exits']:
            current_room = room['exits']['dolu']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

        return current_room


class DropItem(Command):
    def __init__(self):
        super().__init__("poloz", "Položí predmet v miestnosti.")

    def exec(self, current_room:str, world:dict, backpack:list):
        room = world[current_room]
        for item in backpack:
            if item['name'] == name:
                room['items'].append(item)
                backpack.remove(item)
                print(f'{item["name"]} si vyložil z batohu.')
                break
        else:
            print('Taký predmet u seba nemáš.')


class TakeItem(Command):
    def __init__(self):
        super().__init__("poloz", "Vezme predmet z miestnosti.")

    def exec(self, current_room:str, world:dict, backpack:list):
        room = world[current_room]
        for item in room['items']:
            if item['name'] == name:
                if 'movable' not in item['features']:
                    print('Tento predmet sa nedá vziať.')
                elif len(backpack) >= 1:
                    print('Batoh je plný.')
                else:
                    backpack.append(item)
                    room['items'].remove(item)
                    print(f'{item["name"]} si vložil do batohu.')

                break  # return
        else:
            print('Taký predmet tu nikde nevidím.')


class ExamineItem(Command):
    def __init__(self):
        super().__init__("preskumaj", "Preskúma zvolený predmet.")

    def exec(self, current_room:str, world:dict, backpack:list):
        room = world[current_room]
        items = room['items'] + backpack

        for item in items:
            if item['name'] == name:
                print(item['description'])
                return

        print('Taký predmet tu nikde nevidím.')


def use_whip(world: dict, current_room: str, backpack: list):
    if current_room != 'nad priepastou':
        print('Svihol si bičíkom vo vzduchu. Ale švihá, pomyslel si si. Ako za mladých čias.')
        return

    room = world[current_room]
    # pridanie prechodu z miestnosti na vychod
    room['exits']['vychod'] = 'chram'

    # vyhodenie bica z miestnosti alebo z batohu
    for item in backpack:
        if item['name'] == 'bic':
            backpack.remove(item)
            break
    else:
        for item in room['items']:
            if item['name'] == 'bic':
                room['items'].remove(item)
                break

    print(
        'Rozohnal si sa, vzduchom to zasvišťalo a tvoj bič sa zachytil o visiaci konár v hornej časti jaskyne. Prehupnúť sa na druhú stranu už nebude žiadny problém.')


class UseItem(Command):
    def __init__(self):
        super().__init__("pouzi", "Použije zvolený predmet.")

    def exec(self, current_room:str, world:dict, backpack:list):
        room = world[current_room]
        items = room['items'] + backpack

        for item in items:
            if item['name'] == name:
                if 'usable' not in item['features']:
                    print('Tento predmet sa nedá použiť')
                    return

                if name == 'bic':
                    use_whip(world, current_room, backpack)
                    return

        print('Taký predmet tu nikde nevidím.')
