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
            print(f'zobazujem informacie o predmete {self.param}')
            return states.PLAYING
