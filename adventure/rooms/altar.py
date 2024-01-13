from adventure.items import Diamond
from . import directions
from .room import Room


class Altar(Room):
    def act(self, context):
        # count the number of diamonds in room
        counter = 0
        for item in context.backpack:
            if isinstance(item, Diamond) is True:
                counter += 1

        # if the number of diamonds is 5, then open
        if counter == 5:
            context.current_room.exits[directions.DOWN] = 'faraónova hrobka'
            print('Uprostred oltára sa otvoril otvor vedúci do podzemia!')
