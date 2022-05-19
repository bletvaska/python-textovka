from dataclasses import dataclass

from items.features import USABLE, MOVABLE


@dataclass
class Bucket:
    name = 'vedro'
    description = 'Vedro plné vody. Ťažko povedať, či aj pitnej.'
    features = [MOVABLE, USABLE]
