from .command import Command


class Examine(Command):
    name = 'preskumaj'
    description = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        # if no item was given
        if self.param == '':
            print('Neviem, čo chceš preskúmať.')

        # if item is not in backpack
        else:
            for item in context.backpack:
                if item.name == self.param:
                    print(item.description)
                    break
            else:
                print('Taký predmet pri sebe nemáš.')
