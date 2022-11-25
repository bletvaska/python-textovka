# Kokosová palma a uniforma pod ňou

V miestnosti `oáza` sa nachádza kokosová palma. Na jej plody síce Indiana Jones nedosiahne, ale po jej preskúmaní
pod ňou nájde zachovalú nemeckú uniformu. A aby to nebolo všetko, po preskúmaní nemeckej uniformy v nej nájdeme
mosadzný kľúčik.

## Mosadzný kľúčik

Začneme teda vytvorením mosadzného kľúčika. Ten bude mať tieto vlastnosti:

* názov: `kluc`
* opis: `Veľký mosadzný kľúč, zrejme od nejakej truhly.`
* vlastnosti: prenositeľný a použiteľný

Jeho základná implementácia (bez použitia) sa bude nachádzať v balíčku `items` v module `key.py` a vyzerať bude takto:

```python
from dataclasses import dataclass, field

from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Key(Item):
    name: str = 'kluc'
    description: str = 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context):
        return False
```


## Nemecká uniforma

Pokračovať budeme vytvorením nemeckej uniformy, po ktorej preskúmaní objavíme kľúčik.

Nemecká uniforma bude mať tieto vlastnosti:

* názov: `nemecka uniforma`
* opis: `Zachovalá dôstojnícka uniforma.`
* vlastnosti: prenositeľná, použiteľná a preskúmateľná

Uniformu vytvoríme v balíčku `items` v module `nazi_uniform.py`. Základná implementácia (bez použitia uniformy) bude
vyzerať takto:

```python
from dataclasses import dataclass, field

from helpers import get_current_room
from items.features import MOVABLE, USABLE, EXAMINABLE
from items.item import Item
from items.key import Key


@dataclass
class NaziUniform(Item):
    name: str = 'nemecka uniforma'
    description: str = 'Zachovalá dôstojnícka uniforma.'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE, EXAMINABLE])

    def examine(self, context):
        # action
        room = get_current_room(context)
        room.items.append(Key())
        self.features.remove(EXAMINABLE)

        # render
        print('V jednom jej vrecku si objavil kľúč!')

    def use(self, context):
        return False
```


## Kokosová palma

Nakoniec vytvoríme kokosovú palmu, po ktorej preskúmaní objavíme nemeckú uniformu.

Kokosová palma bude mať tieto vlastnosti:

* názov: `kokosova palma`
* opis: `Zdá sa, že na jej plody nedosiahneš.`
* vlastnosti: `EXAMINABLE`


Implementácia palmy sa bude nachádzať v balíčku `items` v module `coconut_palm_tree.py` a jej implementácia bude
vyzerať nasledovne:

```python
from dataclasses import dataclass, field

from helpers import get_current_room
from items.features import EXAMINABLE
from items.item import Item
from items.nazi_uniform import NaziUniform


@dataclass
class CoconutPalmTree(Item):
    name: str = 'kokosova palma'
    description: str = 'Zdá sa, že na jej plody nedosiahneš.'
    features: list = field(default_factory=lambda: [EXAMINABLE])

    def examine(self, context):
        # action
        room = get_current_room(context)
        room.items.append(NaziUniform())
        self.features.remove(EXAMINABLE)

        # render
        print('Pod koreňmi palmy si objavil ukrytú uniformu.')
```

Nakoniec je potrebné kokosovú palmu pridať do miestnosti s názvom `oaza`.
