from .command import Command


class Inventory(Command):
    name = 'inventar'
    description = 'zobrazí obsah hráčovho batohu'

    def exec(self, context) -> str:
        pass
