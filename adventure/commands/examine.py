from .command import Command


class Examine(Command):
    name = 'preskumaj'
    description = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print('Neviem, čo chceš preskúmať.')

        # search for item
        else:
            # item = get_item_by_name(param, context.backpack)

            # search for item in backpack
            for item in context.backpack:
                if item.name == self.param:
                    print(item.description)
                    break
            else:
                # search for item in current room
                for item in context.current_room.items:
                    if item.name == self.param:
                        print(item.description)
                        break
                else:
                    # not found
                    print('Taký predmet tu nikde nevidím.')
