from commands.command import Command
from items.mixins import Movable


class Take(Command):
    def __init__(self):
        super().__init__('vezmi', 'vezme predmet z miestnosti a vloží si ho do batohu.')

    def exec(self, context):
        # ak nebol zadany prikaz s nazvom predmetu
        if len(self._params) == 0:
            print('Neviem, aký predmet chceš vziať.')
            return

        # zisti, ci sa predmet uplnou nahodou nenachadza v batohu
        if self._params in context.backpack:
            print(f'Predmet {self._params} sa už nachádza v batohu.')
            return

        try:
            # zisti, ci sa predmet nachadza v miestnosti
            for item in context.current_room._items:
                if item._name == self._params:
                    # zisti, ci sa da zobrat
                    if isinstance(item, Movable):
                        # zober
                        context.backpack += item
                        context.current_room._items.remove(item)
                        print(f'Do batôžku si si vložil {item._name}.')
                    else:
                        print('Tento predmet sa nedá zobrať.')
                    break
            else:
                print('Taký predmet tu nikde nevidím.')

        except:
            print('Batoh je plny.')

