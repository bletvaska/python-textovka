from game_context import GameContext


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

    def exec(self, context:GameContext):
        pass


class About(Command):
    def __init__(self):
        super().__init__('o hre', 'Túto hru spáchal mirek v roku 2019. Celkom fajnú.')

    def exec(self, context):
        print(self._description)


class LookAround(Command):
    def __init__(self):
        super().__init__('rozhliadni sa', 'Vypíše opis miestnosti.')

    def exec(self, context):
        show_room(context.world[context.current_room])


class Inventory(Command):
    def __init__(self):
        super().__init__('inventar', 'Zobrazí obsah batohu.')

    def exec(self, context):
        if len(context.backpack) > 0:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'     {item["name"]}')
        else:
            print('Batoh je prázdny.')


class Help(Command):
    def __init__(self):
        super().__init__('pomoc', 'Zobrazí pomocníka k jednotlivým príkazom')

    def exec(self, context):
        print('ta pomoz si sam.')


class Commands(Command):
    def __init__(self):
        super().__init__('prikazy', 'Zobrazí zoznam príkazov.')

    def exec(self, context):
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


class Quit(Command):
    def __init__(self):
        super().__init__('koniec', 'Ukončí hru.')

    def exec(self, context):
        print('ta diky ze si si zahral tuto mocnu hru, lebo je fakt mocna.')
        context.state = 'quit'


class East(Command):
    def __init__(self):
        super().__init__("vychod", "Presunie sa na vychod.")

    def exec(self, context):
        """
        Enter the room on east from current room.
        If there is no exit to the east, then no change. The new room will be returned from the function.
        :param world: the world the player is in
        :param current_room: the name of current room player is in
        :return: the name of new room on the east
        """
        room = context.world[context.current_room]

        if 'vychod' in room['exits']:
            context.current_room = room['exits']['vychod']
            show_room(context.world[context.current_room])
        else:
            print('tam sa neda ist')


class West(Command):
    def __init__(self):
        super().__init__("zapad", "Presunie sa na západ.")

    def exec(self, context):
        room = context.world[context.current_room]

        if 'zapad' in room['exits']:
            context.current_room = room['exits']['zapad']
            show_room(context.world[context.current_room])
        else:
            print('tam sa neda ist')


class North(Command):
    def __init__(self):
        super().__init__("sever", "Presunie sa na sever.")

    def exec(self, context):
        room = context.world[context.current_room]

        if 'sever' in room['exits']:
            context.current_room = room['exits']['sever']
            show_room(context.world[context.current_room])
        else:
            print('tam sa neda ist')


class South(Command):
    def __init__(self):
        super().__init__("juh", "Presunie sa na juh.")

    def exec(self, context):
        room = context.world[context.current_room]

        if 'juh' in room['exits']:
            context.current_room = room['exits']['juh']
            show_room(context.world[context.current_room])
        else:
            print('tam sa neda ist')


class Down(Command):
    def __init__(self):
        super().__init__("dolu", "Presunie sa dolu.")

    def exec(self, context):
        room = context.world[context.current_room]

        if 'dolu' in room['exits']:
            context.current_room = room['exits']['dolu']
            show_room(context.world[context.current_room])
        else:
            print('tam sa neda ist')


class DropItem(Command):
    def __init__(self):
        super().__init__("poloz", "Položí predmet v miestnosti.")

    def exec(self, context):
        room = context.world[context.current_room]
        for item in context.backpack:
            if item['name'] == name:
                room['items'].append(item)
                context.backpack.remove(item)
                print(f'{item["name"]} si vyložil z batohu.')
                break
        else:
            print('Taký predmet u seba nemáš.')


class TakeItem(Command):
    def __init__(self):
        super().__init__("vezmi", "Vezme predmet z miestnosti.")

    def exec(self, context):
        room = context.world[context.current_room]
        for item in room['items']:
            if item['name'] == name:
                if 'movable' not in item['features']:
                    print('Tento predmet sa nedá vziať.')
                elif len(context.backpack) >= 1:
                    print('Batoh je plný.')
                else:
                    context.backpack.append(item)
                    room['items'].remove(item)
                    print(f'{item["name"]} si vložil do batohu.')

                break  # return
        else:
            print('Taký predmet tu nikde nevidím.')


class ExamineItem(Command):
    def __init__(self):
        super().__init__("preskumaj", "Preskúma zvolený predmet.")

    def exec(self, context):
        room = context.world[context.current_room]
        items = room['items'] + context.backpack

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

    def exec(self, context):
        room = context.world[context.current_room]
        items = room['items'] + context.backpack

        for item in items:
            if item['name'] == name:
                if 'usable' not in item['features']:
                    print('Tento predmet sa nedá použiť')
                    return

                if name == 'bic':
                    use_whip(context.world, context.current_room, context.backpack)
                    return

        print('Taký predmet tu nikde nevidím.')
