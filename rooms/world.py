from .airplane import Airplane
from .free_fall import FreeFall


def get_world():
    return [
        Airplane(),
        FreeFall(),
    ]
