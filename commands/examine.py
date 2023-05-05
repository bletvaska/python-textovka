from .command import Command


class Examine(Command):
    name = 'preskumaj'
    description = 'preskúma zvolený predmet'

    def exec(self, context):
        print(f'skumam predmet {self.param}')
