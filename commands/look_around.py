from dataclasses import dataclass

from .command import Command


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'vypíše opis miestnosti, v ktorej sa hráč nachádza'

    def exec(self, context: dict, arg: str):
        """
        Prints description about the room

        Prints out the description about the room given as parameter.
        :param room: room to describe
        """
        room = context['room']

        print(f'Nachádzaš sa v miestnosti {room["name"]}')
        print(room['description'])

        # print items in the room
        if room['items'] == []:  # len(room['items'] == 0
            print('Nevidíš tu nič zvláštne.')
        else:
            print("Vidíš:")
            for item in room['items']:
                print(f'\t* {item["name"]}')

        # print exits
        exits = []
        for _exit in room['exits']:
            if room['exits'][_exit] is not None:
                exits.append(_exit)

        if exits == []:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            print('Môžeš ísť:')
            for ex in exits:
                if ex == 'north':
                    print('\t* sever')
                if ex == 'south':
                    print('\t* juh')
                if ex == 'east':
                    print('\t* východ')
                if ex == 'west':
                    print('\t* západ')
