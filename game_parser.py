from commands import cmd_about, cmd_commands, cmd_drop, cmd_east, cmd_explore, cmd_inventory, cmd_look_around, cmd_north, cmd_quit, cmd_south, cmd_take, cmd_use, cmd_west

commands = [
    {
        'name': 'inventar',
        'description': 'Zobrazí obsah hráčovho batohu',
        'aliases': ['inventar', 'inventory', 'i'],
        'exec': cmd_inventory
    },

    {
        'name': 'o hre',
        'description': 'Zobrazí informácie o autorovi hry a o hre samotnej.',
        'aliases': ['o hre', 'about', 'info'],
        'exec': cmd_about
    },

    {
        'name': 'rozhliadni sa',
        'description': 'Vypíše obsah aktuálnej miestnosti.',
        'aliases': ['rozhliadni sa', 'look around'],
        'exec': cmd_look_around
    },

    {
        'name': 'koniec',
        'description': 'Ukončí rozohratú hru.',
        'aliases': ['koniec', 'quit', 'end', 'q'],
        'exec': cmd_quit
    },

    {
        'name': 'preskumaj',
        'description': 'Preskúma zvolený predmet.',
        'aliases': ['preskumaj', 'explore'],
        'exec': cmd_explore,
    },

    {
        'name': 'vezmi',
        'description': 'Vezme predmet z miestnosti do batohu.',
        'aliases': ['vezmi', 'zober', 'take'],
        'exec': cmd_take,
    },

    {
        'name': 'poloz',
        'description': 'Vyloží predme z batohu do aktuálnej miestnosti.',
        'aliases': ['poloz', 'drop'],
        'exec': cmd_drop,
    },

    {
        'name': 'prikazy',
        'description': 'Zobrazí zoznam dostupných príkazov v hre.',
        'aliases': ['prikazy', 'commands'],
        'exec': cmd_commands,
    },

    {
        'name': 'pouzi',
        'description': 'Použije daný predmet.',
        'aliases': ['pouzi', 'use', 'u'],
        'exec': cmd_use
    },

    {
        'name': 'sever',
        'description': 'Presunie sa do miestnosti na sever.',
        'aliases': ['sever', 'north'],
        'exec': cmd_north
    },

    {
        'name': 'juh',
        'description': 'Presunie sa do miestnosti na sever.',
        'aliases': ['juh', 'south'],
        'exec': cmd_south
    },

    {
        'name': 'vychod',
        'description': 'Presunie sa do miestnosti na sever.',
        'aliases': ['vychod', 'east'],
        'exec': cmd_east
    },

    {
        'name': 'zapad',
        'description': 'Presunie sa do miestnosti na sever.',
        'aliases': ['zapad', 'west'],
        'exec': cmd_west
    }

]


# ! FIXME zamysliet sa nad jednopismenkovymi prikazmi
def parse(line: str, commands: list) -> dict:
    # walk throught the list of commands
    for cmd in commands:
        for alias in cmd['aliases']:

            if line.startswith(alias):
                # extract parameter, if cmd was found
                cmd['param'] = line[len(alias):].strip()
                return cmd

    return None
