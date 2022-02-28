import json
from dataclasses import dataclass
from typing import List

from .command import Command
from context import Context


@dataclass
class Save(Command):
    name: str = 'uloz'
    # aliases: List[str]
    description: str = 'uloží aktuálny stav hry do súboru'

    def exec(self, context: Context, path: str):
        # je historia prazdna?
        if len(context.history) == 0:
            print('Zatiaľ nie je čo ukladať.')
            return

        # bol zadany subor na ulozenie?
        if path == '':
            print('Neviem, do akého súboru chceš stav hry uložiť.')
            return

        try:
            with open(path, 'w') as file:
                json.dump(context.history, file)
                print(f'Stav hry bol úspešne uložený do súboru {path}.')
        except PermissionError:
            print(f'Chyba: nemáš dostatočné práva na uloženie stavu hry do súboru {path}.')
        except FileNotFoundError:
            print(f'Chyba: cesta k súboru {path} neexistuje.')
        except IsADirectoryError:
            print(f'Chyba: cesta {path} je priečinok.')
        except Exception as ex:
            print('Chyba: Pri ukladaní stavu do súboru došlo k chybe.')
            print(type(ex))
