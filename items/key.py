from items import Item


class Key(Item):
    def __init__(self):
        super().__init__('klucik', 'Veľmi používaný kľúčik značky FAB.', ['movable', 'usable'])

    def use(self, context):
        print('pouzivam predmet klucik.')
        # 1. zistim, ci v aktualnej miestnosti sa nachadzaju 'zamknute dvere'
        
        # 2. vytvorim prechod z miestnosti do batozinoveho priestoru
        # 3a. zmenim stav dveri prepisanim ich nazvu a opisu
        # 3b. slabe panty, dvere aj s klucik vycuclo vonku z lietadla. to bol ale rachot.