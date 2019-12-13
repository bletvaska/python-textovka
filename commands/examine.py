from commands.command import Command


class Examine(Command):
    def __init__(self):
        super().__init__('preskumaj', 'preskúma zvolený predmet.')

    def exec(self, context):
        # ak nebol zadany prikaz s nazvom predmetu
        if len(self._params) == 0:
            print('Neviem, aký predmet chceš preskúmať.')
            return

        # zisti, ci sa predmet nachadza v miestnosti
        items = context.current_room._items + context.backpack
        for item in items:
            if item._name == self._params:
                print(item)
                break
        else:
            print('Taký predmet tu nikde nevidím.')
