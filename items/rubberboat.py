from items import Item


class RubberBoat(Item):
    def __init__(self):
        super().__init__('gumenny cln', 'Gumenný čln na plávanie.', ['movable', 'usable'])

    def use(self, context):
        # 1. ak nie som v miestnosti 'vo vzduchu', tak nemozem cln nafuknut
        if context.current_room._name != 'vo vzduchu':
            print('Nemáš tu dosť miesta na nafúknutie člnu.')
            return

        # 2. vyhodim cln z batohu / z miestnosti
        if self._name in context.backpack:
            context.backpack -= self
        else:
            context.current_room._items.remove(self)

        # 3. zmenim aktualnu miestnost na miestnost 'zem'
        context.current_room = context.world['pristav']

        # 4. mocny text
        print('Červený text pri špagáte znel jasne - POTIAHNUŤ. Tak si potiahol a nafúkol si čln. Zrejme by to dalo zabrať nafúkať vlastnými silami. Počas čakania a voľného letu teda pádu vzduchom ti tvoju náladu prerušil iba mohutný výbuch parkujúceho lietadla do neďalekého kopca.')

        print('Voľným pádom si sa priblížil k zemi. Zasánkoval si si, zletel si z ďalšieho útesu, zaplával si si a bezpečne si pristál pri brehu. Po vystúpení z člna si sa s ním rozlúčil slovami "Kurnik. Narazil som si zadok!"')

        # 5. rozhliadni sa
        print(context.current_room)