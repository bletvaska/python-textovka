def use_canister(canister, current_room):
    # som v miestnosti, kde su dvere?
    if current_room['name'] != 'chodba':
        print(
            'Neviem, čo by som tu s tým kanistrom plným benzínu tak mohol poliať')
        return

    # som v miestnosti s dverami - idem ich poliat
    for item in current_room['items']:
        if item['name'] == 'vchodove dvere':
            current_room['items'].remove(item)
            break

    # vlozim do miestnosti novy predmet - poliate dvere
    door = {
        'name': 'poliate dvere',
        'description': 'Vchodové dubové dvere, ktoré sú stále rovnako masívne ako predtým, akurát teraz ešte voňajú po benzíne.',
        'features': []
    }
    current_room['items'].append(door)

    # zmenim stav kanistru - zmenim opis a nebude pouzitelny
    canister['description'] = 'Kanister na benzín, v ktorom už nie je ani kvapka'
    canister['features'].remove('usable')

    # vypisem spravu do hry
    print(
        'Odšroboval si zátku na kanistri a celý jeho obsah si vylial na vchodové dvere. Hmm... Je to teraz lepšie, pomyslel si si. Také voňavejšie...')


def use_matches():
    # ak sa nenachdzam v miestnosti s poliatymi dverami (v chodbe), tak napisem hlasku:
    # nemam si co zapalit.
    # a skoncim

    # odstranim z miestnosti poliate dvere a nahradim ich horiacimi dverami

    # vyhodim zapalky z batohu, lebo sa minuli

    # vypisat hlasku o tom, co som spachal
    # skrtol si zapalkou blizko dveri, ktore vonali benzinom a co sa nestalo - preskocila iskra. dvere okamzite zblkli a ty si radsej odstupil trosku spat.
    pass


def use_bucket():
    pass
