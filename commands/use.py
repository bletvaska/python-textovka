from dataclasses import dataclass

from context import Context
from features import USABLE
from usages import use_canister, use_matches, use_bucket, use_newspaper
from utils import get_item_by_name
from .command import Command


@dataclass
class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet'

    def exec(self, context: Context, arg: str):
        item_name = arg
        backpack = context.backpack['items']
        room = context.room

        # is there name given?
        if item_name == '':
            print('Neviem čo chceš použiť.')
            return

        # is there such item?
        item = get_item_by_name(item_name, backpack + room['items'])
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is item usable?
        if USABLE not in item['features']:
            print('Tento predmet sa nedá použiť')
            return

        # using the item
        # update history
        context.history.append(f'POUZI {item_name}')

        # item['exec'](context, item)
        if item_name == 'kanister':
            use_canister(context, item)

        elif item_name == 'zapalky':
            use_matches(context, item)

        elif item_name == 'vedro':
            use_bucket(context, item)

        elif item_name == 'noviny':
            use_newspaper(context, item)

        else:
            # print(f'Použil si predmet {item["name"]}')
            raise NotImplementedError(f'Usage of item "{item["name"]}" was not yet implemented')