# from context import Context
from items import Item


class Key(Item):
    def __init__(self):
        super().__init__('klucik', 'Veľmi používaný kľúčik značky FAB.', ['movable', 'usable'])

    def use(self, context):
        # 1. zistim, ci v aktualnej miestnosti sa nachadzaju 'zamknute dvere'
        for item in context.current_room._items:
            if item._name == 'zamknute dvere':
                # 2. vytvorim prechod z miestnosti do batozinoveho priestoru
                context.world['prva trieda'].add_exit('east', context.world['batozinovy priestor'])

                # 3a. zmenim stav dveri prepisanim ich nazvu a opisu
                # item._name = 'odomknute dvere'

                # 3b. slabe panty, dvere aj s klucik vycuclo vonku z lietadla. to bol ale rachot.
                context.current_room._items.remove(item)
                if self._name in context.backpack:
                    context.backpack -= self
                else:
                    context.current_room._items.remove(self)
                print('Pristúpil si k dverám a z batohu si vytiahol kľúčik značky FAB. Vložil si ho do zámky a otočil. Povolil. Ale s ním povolili celé dvere. S rachotom sebe vlastným opustili lietadlo otvorenými dverami.')

                # 4. klucik znefunkcnime tym, ze vyhodime ficuru 'usable' zo zoznamu ficur
                # self.features.remove('usable')

                # print('Pristúpil si k dverám a z batohu si vytiahol kľúčik značky FAB. Vložil si ho do zámky a otočil. Povolil. Dvere sa vŕzgavo otvorili.')
                break
        else:
            print('Ta nevidím, kde by som ten kľúčik mohol štúriť.')


