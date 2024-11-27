from .command import Command


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        # if not item was entered
        if self.param == '':
            print('Neviem, čo chceš preskúmať.')
            return

        # search for item and print description if found
        for item in context.current_room.items:
            if item.name == self.param:
                print(item.description)
                return

        # not found
        print('Taký predmet tu nikde nevidím.')
