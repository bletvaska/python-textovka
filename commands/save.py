from commands.command import Command


class Save(Command):
    def __init__(self):
        super().__init__('uloz', 'Uloží stav hry do súboru.')

    def exec(self, context):
        # ak nebol zadany prikaz s nazvom suboru
        if len(self._params) == 0:
            print('Chýba názov súboru.')
            return

        # uloz subor riadok po riadku
        with open(self._params, 'w') as f:
            for cmd in context.history:
                f.write(f'{cmd}\n')

        # vypis spravu pre pouzivatela
        print('Hra bola úspešne uložená.')