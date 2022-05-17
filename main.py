#!/usr/bin/env python
from dataclasses import dataclass

import states


@dataclass
class Room:
    name: str
    description: str
    items: list[str]
    exits: list[str]

    def show(self):
        print(f'Nachádzaš sa v miestnosti {self.name}.')
        print(self.description)

        # show items
        if len(self.items) == 0:
            print('Nevídiš tu nič zvláštne.')
        else:
            print('Vidíš: ', end='')
            print(', '.join(self.items))

        # show exits
        if len(self.exits) == 0:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            print('Východy z miestnosti:')
            for ext in self.exits:
                print(f'  {ext}')


def intro():
    """
    Shows the intro screen of the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('                        and his Great Escape')
    print()


def outro():
    """
    Shows the outro screen of the game.
    """
    print('(c)2022 by mirek')
    print('See you soon.')


def main():
    # game init
    game_state = states.PLAYING
    backpack = ['bic', 'revolver']

    room = Room(name='dungeon',
                description='Nachádzaš sa vo veľmi tmavej miestnosti. Kamenné múry dávajú tušiť, že sa'
                            'nachádzaš v nejakej kamennej kobke. Žeby podzemie hradu v Grunwalde? '
                            'Okná tu nie sú žiadne, čo by ťa uistilo o správnosti tohto predpokladu.',
                items=[
                    'zapalky',
                    'vedro',
                    'kanister',
                    'dvere'
                ],
                exits=[
                    'sever',
                    'juh'
                ]
                )

    room.show()

    # game loop
    while game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':
            continue

        # rozhliadni sa, look around
        elif line in ('rozhliadni sa', 'look around'):
            room.show()

        # about, info, ?
        elif line in ('o hre', 'about', 'info', '?'):
            print('(c)2022 created by mire(c) z koši(c)')
            print('Ďaľšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')

        # commands, help
        elif line in ('prikazy', 'help', 'commands'):
            print('Zoznam príkazov v hre:')
            print('* koniec - skončenie programu')
            print('* o hre - vypíše info o hre')
            print('* prikazy - vypíše zoznam príkazov')
            print('* rozhliadni sa - vypíše opis aktuálnej miestnosti')

        # quit, exit, q, bye
        elif line in ('koniec', 'quit', 'exit', 'q', 'bye'):
            print('Naozaj chceš skončiť? (a/n)')
            line = input('>> ').lower().strip()
            if line in ('a', 'ano', 'y', 'yes'):
                print('Dakujem, ze si si zahral tuto fantasticku hru. Príď aj nabudúce.')
                game_state = states.QUIT
            else:
                continue

        else:
            print('Taký príkaz nepoznám.')


if __name__ == '__main__':
    intro()
    main()
    outro()
