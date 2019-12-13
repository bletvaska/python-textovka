from commands.command import Command


class Drop(Command):
    def __init__(self):
        super().__init__('poloz', 'polozí predmet z batohu do miestnosti.')

    def exec(self, context):
        # ak nebol zadany prikaz s nazvom predmetu
        if len(self._params) == 0:
            print('Neviem, aký predmet chceš položiť.')
            return

        # zisti, ci sa uz predmet uplnou nahodou nenachdza v miestnosti
        for item in context.current_room._items:
            if item._name == self._params:
                print(f'Predmet {item._name} už v miestnosti voľne leží.')
                return

        # zisti, ci sa predmet nachadza v batohu
        for item in context.backpack:
            if item._name == self._params:
                context.backpack.remove(item)
                context.current_room._items.append(item)
                print(f'Do miestnosti si položil predmet {item._name}.')
                break
        else:
            print('Taký predmet u seba nemáš.')

