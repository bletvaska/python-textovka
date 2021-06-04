import random


class Item(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.features = []

    def __str__(self):
        return f'{self.name} - {self.description}'


class Knife(Item):
    def __init__(self):
        super().__init__('nožík', 'ostrá rybka jak fras')
        self.features.append('movable')


class Newspaper(Item):
    def __init__(self):
        super().__init__('noviny', 'Nové tajmsy. Ale nebars aktuálne.')
        self.features.append('usable')
        self.features.append('movable')

    def use(self, context):
        news = [
            '"Bláha je najinteligentnejší človek, s ktorým som sa stretol.". Tak sa vyjadril Preceda po dvanástich štamprlíkoch.',
            'Počasie na dnes: Ráno hmlysto, na obed takisto a večer tma.',
            'Naši hokejisti to žial nezvládli. Po prehre s USA odchádzajú domov. Ikarusom.'
        ]

        print(f'Roztvoril si nové tajmsy a začítal si sa. Hmm... {random.choice(news)}')
