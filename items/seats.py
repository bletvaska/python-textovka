from items import Item


class Seats(Item):
    def __init__(self):
        super().__init__('sedacky', 'Mäkké, jemné, spružiny trčiace sedačky lietadla. Ako nové. A len pre pilota.', ['examinable'])

    def examine(self, context):
        print('ta preskumavam sedacky. podrobne.')