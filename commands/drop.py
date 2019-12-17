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
        if self._params not in context.backpack:
            print('Taký predmet u seba nemáš.')
            return

        # poloz predmet
        item = context.backpack[self._params]
        context.backpack -= item
        context.current_room._items.append(item)
        print(f'Do miestnosti si položil predmet {item._name}.')

        # ulozi prikaz do historie
        self.save_to_history(context)


