from commands.command import Command


class Use(Command):
    def __init__(self):
        super().__init__('pouzi', 'použije zvolený predmet.')

    def exec(self, context):
        # ak nebol zadany prikaz s nazvom predmetu
        if len(self._params) == 0:
            print('Neviem, aký predmet chceš použiť.')
            return

        # zisti, ci sa predmet nachadza v miestnosti alebo v batohu
        items = context.current_room._items + context.backpack._items
        for item in items:
            if item._name == self._params:
                if 'usable' in item.features:
                    item.use(context)

                    # ulozi prikaz do historie
                    self.save_to_history(context)
                else:
                    print('Tento predmet sa nedá použiť.')
                break
        else:
            print('Taký predmet tu nikde nevidím.')
