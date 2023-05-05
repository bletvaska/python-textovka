from .command import Command


class Examine(Command):
    name = 'preskumaj'
    description = 'preskúma zvolený predmet'

    def exec(self, context):
        # when no param was given
        # len(self.param) == 0
        if self.param == '':
            print('Neviem, aký predmet chceš preskúmať.')

        else:

            for item in context.current_room.items:
                if item.name == self.param:
                    print(item.description)
                    break
            else:
                for item in context.backpack:
                    if item.name == self.param:
                        print(item.description)
                        break

                else:
                    print('Taký predmet tu nikde nevidím.')

