import json

from .command import Command


class Save(Command):
    name = 'uloz'
    description = 'uloží rozohratú hru do súboru'

    def exec(self, context):
        with open('save.json', 'w') as file:
            json.dump(context.dict(), file, ensure_ascii=False, indent=4)

        print('Aktuálny stav bol uložený do súboru save.json')
