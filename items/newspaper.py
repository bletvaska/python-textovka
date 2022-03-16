from dataclasses import dataclass
import random

from context import Context
from items.features import MOVABLE, USABLE
from .item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'dennik sme s autorskou strankou sama marca'

    def __post_init__(self):
        self.features += [MOVABLE, USABLE]

    def use(self, context: Context):
        print('Včerajšie vydanie Denníka N. Čo nové sa deje vo svete? Zalistoval si a… je to tu…')

        titles = [
            "Exminister Drucker: Hlas a Smer stratili obsah a pridali sa k antisystému",
            "Mal som dobré známky, tak som z dediny na severe Vietnamu mohol prísť do Komárna",
            "Newsfilter: Kažimír odkázal prezidentke, že on nikam neodchádza",
            "Ekonomický newsfilter: Distribučky sa vzbúrili, Sulík nemá na výber, škody zaplatí štát"
        ]

        print(random.choice(titles))
