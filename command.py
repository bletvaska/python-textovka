import states


class Command(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.aliases = []
        self.params = None

    def exec(self, context):
        raise NotImplementedError('Táto funkcia ešte nebola implementovaná.')

    def __str__(self):
        return f'{self.name} - {self.description}'


class About(Command):
    def __init__(self):
        super().__init__('o hre', 'zobrazí informácie o hre')
        self.aliases.append('about')
        self.aliases.append('o hre')

    def exec(self, context):
        print('ta mocna hra')
        print('tvojou ulohou je ju dohrat a sa neosalit')
        print('tuto mocnu hru vytvoril (c)2021 mirek')


class Use(Command):
    def __init__(self):
        super().__init__('pouzi', 'pouzije predmet')
        self.aliases.append('use')
        self.aliases.append('pouzi')

    def exec(self, context):
        room = context.room
        inventory = context.inventory

        # step 1: neviem, co mam preskumat
        if len(self.params) == 0:
            print('Neviem, čo mám použiť.')
        else:
            # step 3: {description}
            for item in room.items + inventory:
                if item.name == self.params:
                    if 'usable' in item.features:
                        item.use(context)
                    else:
                        print('Tento predmet sa nedá použiť.')
                    return

            else:
                print('Taký predmet tu nikde nevidím.')


class Quit(Command):
    def __init__(self):
        super().__init__(
            'koniec',
            'ukončí rozohratú hru'
        )
        self.aliases.append('koniec')
        self.aliases.append('quit')

    def exec(self, context):
        print('Ta končíme')
        context.state = states.STATE_EXIT
