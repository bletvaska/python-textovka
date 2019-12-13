from commands.command import Command


class About(Command):
    def __init__(self):
        super().__init__('o hre', 'zobrazí informácie o hre')

    def exec(self, context=None):
        print(
            'ta to je iny sumny mladenec toten autor. by si ho mohol podporit mocnym fsimnym na ucet SK1234567890. ale fakt mocnym.')
        print('to je asi fsetko, co by si o nom mohol vediet. verejne.')
