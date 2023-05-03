from states import STATE_PLAYING, STATE_QUIT

print("Indiana Jones and his Greatest Python Adventure")
game_state = STATE_PLAYING

while game_state == STATE_PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    elif line == 'o hre':
        print('Túto mocnú hru spáchal mocný programátor mirek')
        print('(c)2023 by mirek')

    elif line == 'pre evku':
        print('toto je vyrobene vylucne pre evku.')

    elif line == 'prikazy':
        print('Zoznam dostupnych prikazov v hre:')
        print('* o hre - zobrazi informacie o hre')
        print('* prikazy - zobrazi zoznam dostupnych prikazov')

    elif line == 'koniec':
        question = input('Naozaj chceš skončiť? (ano/nie) ').lower().strip()
        if question == 'ano':
            print('Díky, že si si zahral túto mocnú hru.')
            game_state = STATE_QUIT

    else:
        print('Taký príkaz nepoznám.')

print('koniec')
