#!/usr/bin/env python3

class Room:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._exits = {}

    def __str__(self) -> str:
        return self._name

    def __repr__(self):
        return f'repr: "{self._name}". {self._description}'


world = {}

Room('prva trieda', '')

kabina = Room('kabina', 'Vošiel si do kabíny pilotov, ktorá sa skrývala za voľne zatiahnutým závesom. Aj tu je kľud. Nikto tu nie je. Kniple sa voľne pohupujú a ručičky na budíkoch sa voľne otáčajú.')

vovzduchu = Room('vo vzduchu', 'Voľne sa vznášaš v priestore a vychutnávaš si ostrý vzduch. Tvoju pozornosť rozptyľujú len zväčšujúce sa bodky na zemi. Krásne je dnes vonku.')

prvatrieda = Room('prva trieda', 'Prvá trieda. Sliepky a iné živočíchy tu cestujú s tebou tiež. Na sedadlách sa nachádzajú klietky a iný spotrebný materiál.')

spajza = Room('batozinovy priestor', 'Veľa priestoru pre padáky. Škoda, že tu žiadny nevidno.')



print('Indiana Jones and the Plane Escape')

print(
    'Ta si sa zobudil v prvej triede lietadla spoločnosti Lao Che. To ticho ti až bilo do uší. Lietadlo vraj nikto nešoféruje a aj motory sú už vypnuté.')

while True:
    line = input('> ').strip().lower()

    if line in ('koniec', 'quit', 'k', 'q'):
        break

    elif line in ('o autorovi', 'o mne', 'info'):
        print(
            'ta to je iny sumny mladenec toten autor. by si ho mohol podporit mocnym fsimnym na ucet SK1234567890. ale fakt mocnym.')
        print('to je asi fsetko, co by si o nom mohol vediet. verejne.')

    elif line in ('prikazy', 'prikaz', 'commands'):
        print('Zoznam prikazov:')
        print('\tkoniec - ukonci tuto mocnu hru')
        print('\to autorovi - zobrazi info o autorovi')
        print('\tprikazy - zobrazi zoznam prikazov')

    elif line in ('zapad', 'z', 'west', 'w'):
        print(
            'Vošiel si do kabíny pilotov, ktorá sa skrývala za voľne zatiahnutým závesom. Aj tu je kľud. Nikto tu nie je. Kniple sa voľne pohupujú a ručičky na budíkoch sa voľne otáčajú.')

    elif line in ('vychod', 'v', 'east', 'e'):
        print(
            'Prvá trieda. Sliepky a iné živočíchy tu cestujú s tebou tiež. Na sedadlách sa nachádzajú klietky a iný spotrebný materiál.')

    elif line in ('dolu', 'down'):
        print(
            'Voľne sa vznášaš v priestore a vychutnávaš si ostrý vzduch. Tvoju pozornosť rozptyľujú len zväčšujúce sa bodky na zemi. Krásne je dnes vonku.')

    # elif line in ('east', 'vychod'):
    #     print('')

    else:
        print('taky prikaz nepoznam.')
