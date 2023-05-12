from . import directions
from .airplane import Airplane
from .free_fall import FreeFall
from .room import Room


def get_world():
    return [
        Airplane(),
        FreeFall(),
        Room(
            name='púšť',
            description='Si na púšti, ktorá sa vyznačuje predovšetkým, že je pustá. (Je zaujímavé, že to tu vyzerá úplne inak, ako v lietadle.)',
            exits={
                directions.NORTH: 'púšť',
                directions.EAST: 'púšť',
                directions.WEST: 'púšť',
                directions.SOUTH: 'oáza'
            }
        )
    ]
