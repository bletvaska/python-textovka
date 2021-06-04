import json

import states
from item import Knife, Newspaper
from room import Room


class GameContext:
    def __init__(self):
        self.state = states.STATE_PLAYING
        self.inventory = []
        self.inventory_capacity = 2

        self.room = Room('tmavá miestnosť', "Stojíš v tmavej miestnosti. Zrejme sa tu už dlho neupratovalo, lebo do nosa sa ti ftiera zepeklitý zápach niečoho zdochnutého. Ani len svetlo nepreniká cez zadebnené okná. I have a bad feeling about this place, ako by klasik povedal.")
        self.room.items.append(Knife())
        self.room.items.append(Newspaper())

        # with open('world.json', 'r', encoding='utf-8') as file:
        #     self.world = json.load(file)
