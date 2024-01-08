from states import STATE_PLAYING, STATE_QUIT

print("Indiana Jones and his Greatest Python Adventure")


game_state = STATE_PLAYING
while game_state == STATE_PLAYING:
    line = input('> ').lower().lstrip().rstrip()   # echo line | lower | lstrip | rstrip

    if line == '':  # if len(line) == 0:
        pass  # {}

    elif line == 'o hre':
        print('(c)2024 created by mirek')
        print('Dalsie dobrodruzstvo indiana jonesa tentokrat vytvorene v jazyku Python.')

    elif line == 'prikazy':
        print('V hre je možné použiť tieto príkazy:')
        print('* koniec - ukončí rozhratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')

    elif line == 'koniec':
        print('Ďakujem, že si si zahral túto úžasnú (ukradnutú) hru.')
        game_state = STATE_QUIT

    else:
        print('Taký príkaz nepoznám.')

print('(c)2024 mirek')
