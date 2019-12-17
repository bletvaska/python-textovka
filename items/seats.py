from items import Item, Key


class Seats(Item):
    def __init__(self):
        super().__init__('sedacky', 'Mäkké, jemné, spružiny trčiace sedačky lietadla. Ako nové. A len pre pilota.', ['examinable'])

    def examine(self, context):
        # 1. do miestnosti vlozim klucik
        context.current_room._items.append(Key())

        # 2. zrusim ficuru 'examinable'
        self.features.remove('examinable')

        # 3. mocny text
        print('Neodolal si a svoje veľké dlane si strčil medzi operadlo a sedadlo. Oči ti zažiarili, keď si nahmatal niečo chladné a kovové. V tvojej dlani sa objavil kľúčik. Značky FAB. Nič moc.')