import json
from dataclasses import dataclass

import requests

from context import Context
from .command import Command
import config


@dataclass
class Save(Command):
    name: str = 'uloz'
    description: str = 'uloží rozohratú hru'

    def exec(self, context: Context, arg: str):
        if arg == '':
            print('Neviem, kam chceš stav hry uložiť.')
            return

        if arg == 'cloud':
            # da sa ulozit aj cely context, pretoze je slovnik
            payload = {
                "history": context.history
            }

            headers = {
                'X-Parse-Application-Id': config.app_id,
                'X-Parse-REST-API-Key': config.rest_api_key,
                'Content-Type': 'application/json'
            }

            with requests.post(f'{config.base_url}/history', headers=headers, json=payload) as response:
                data = response.json()
                print(f'Tvoja pozícia má kľúč "{data["objectId"]}".')

            return

        # save to file
        try:
            with open(arg, 'w') as file:
                json.dump(context.history, file)
        except Exception as ex:
            print('CHYBA: Chyba pri zápise do súboru.')
            print(f'CHYBA: {ex}')
