from dataclasses import dataclass

from context import Context


@dataclass
class Commands:
    name: str = 'prikazy'
    description: str = 'vypíše zoznam príkazov'

    def exec(self, context: Context):
        print('Zoznam príkazov v hre:')
        print('* inventar - zobrazí obsah hráčovho batohu')
        print('* koniec - skončenie programu')
        print('* o hre - vypíše info o hre')
        print('* poloz - položí predmet z batohu do aktuálnej miestnosti')
        print('* prikazy - vypíše zoznam príkazov')
        print('* rozhliadni sa - vypíše opis aktuálnej miestnosti')
        print('* vezmi - vezme predmet z miestnosti a vloží si ho do batohu')
