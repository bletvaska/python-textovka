from room import Room


class Context:
    def __init__(self):
        self.game_state = 'PLAYING'
        self.world = {}

        self.world['kabina'] = Room('kabina',
                               'Vošiel si do kabíny pilotov, ktorá sa skrývala za voľne zatiahnutým závesom. Aj tu je kľud. Nikto tu nie je. Kniple sa voľne pohupujú a ručičky na budíkoch sa voľne otáčajú.')

        self.world['vo vzduchu'] = Room('vo vzduchu',
                                   'Voľne sa vznášaš v priestore a vychutnávaš si ostrý vzduch. Tvoju pozornosť rozptyľujú len zväčšujúce sa bodky na zemi. Krásne je dnes vonku.')

        self.world['prva trieda'] = Room('prva trieda',
                                    'Prvá trieda. Sliepky a iné živočíchy tu cestujú s tebou tiež. Na sedadlách sa nachádzajú klietky a iný spotrebný materiál.')

        self.world['batozinovy priestor'] = Room('batozinovy priestor',
                                            'Veľa priestoru pre padáky. Škoda, že tu žiadny nevidno.')

        self.world['kabina'].add_exit('east', self.world['prva trieda'])
        self.world['prva trieda'].add_exit('east', self.world['batozinovy priestor'])
        self.world['prva trieda'].add_exit('west', self.world['kabina'])
        self.world['prva trieda'].add_exit('down', self.world['vo vzduchu'])
        self.world['batozinovy priestor'].add_exit('west', self.world['prva trieda'])

        self.current_room = self.world['prva trieda']