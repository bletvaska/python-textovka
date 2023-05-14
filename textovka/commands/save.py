import json

from .command import Command


class Save(Command):
    name = 'uloz'
    description = 'uloží aktuálny stav hry'

    def exec(self, context):
        file =  open('/tmp/context.json', 'w')
        json.dump(context.dict(), file)
        file.close()

        print('Uspesne som ulozil stav hry.')

        https: // api.openweathermap.org / data / 2.5 / weather?q = kosice & appid =
        9e547051a2a00f2bf3e17a160063002d & units = metric
