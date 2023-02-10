from .command import Command


class Load(Command):
    name = 'nahraj'
    description = 'nahrá uložený stav hry zo súboru'

    def exec(self, context):
        pass
