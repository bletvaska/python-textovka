from .command import Command


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context, param):
        if param == '':
            print('Neviem, čo chceš preskúmať.')
            return

        for item in context.current_room.items:
            if param == item.name:
                print(item.description)
                break
        else:
            print('Taký predmet tu nikde nevidím.')
