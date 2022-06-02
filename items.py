from dataclasses import dataclass
import random


@dataclass
class Item:
    name: str
    description: str


@dataclass
class Whip:
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný kamarát na každom jednom dobrodužstve.'


@dataclass
class Newspaper:
    name: str = 'noviny'
    description: str = 'Posledné vydanie Bravíčka. To najlepšie čítanie pre každého chovateľa Pytóna.'

    def use(self):
        print('Aaaa Bravíčko. Zalistoval si čerstvým vydaním tohto legendárneho časopisu každého správneho Pytonistu '
              'a píšu...')

        headlines = (
            'Python 3.11 bude vydany v piatok 13.',
            'Spravny Pythonista pouziva len Python >= 3.7',
            'import this'
        )

        print(random.choice(headlines))


@dataclass
class Revolver:
    name: str = 'revolver'
    description: str = 'Štandardný revolver značky Smis-end-Weson'
