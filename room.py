class Room:
    def __init__(self, name, description):
        self.description = description
        self.name = name
        self.exits = {}
        self.items = []

    def show_room(self):
        print(f'Nachádzaš sa v miestnosti {self.name}.')
        print(f'{self.description}')

        if len(self.items) == 0:
            print('V miestnosti sa nenachadzaju ziadne predmety.')
        else:
            print(f'V miestnosti si nasiel tieto predmety:')
            for item in self.items:
                print(f'\t* {item.name.lower()}')

        if len(self.exits) == 0:
            print('Z miestnosti neexistujú žiadne východy.')
        else:
            print(f'Východy z miestnosti:')

            for key in self.exits:
                if key == 'north':
                    print(f'\tsever')
                elif key == 'south':
                    print('\tjuh')
                elif key == 'east':
                    print('\tvýchod')
                elif key == 'west':
                    print('\tzápad')
