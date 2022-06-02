from dataclasses import dataclass


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


@dataclass
class Revolver:
    name: str = 'revolver'
    description: str = 'Štandardný revolver značky Smis-end-Weson'
