from items.item import Item
from items.mixins import MovableMixin


class GoldenIdol(Item, MovableMixin):
    def __init__(self):
        super().__init__('zlata soska', 'Zlata soska, medzi ucastnikmi kurzu tiez znama aj ako Golden Idol. Sen nejedneho archeologa. Cela zo zlata a vazi hadam aj zo 10 kil. To by bolo prachov...')