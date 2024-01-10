import states
from commands.command import Command
from rooms.room import Room


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, room: Room) -> str:
        if self.param == '':
            print('Neviem, čo chceš preskúmať.')
            return states.PLAYING
        else:
            for item in room.items:
                if item.name == self.param:
                    print(item.description)
                    return states.PLAYING

            print('Taký predmet tu nikde nevidím.')
            return states.PLAYING
