print("Indiana Jones and his Greatest Python Adventure")
line = input('> ')

if line == '':  # if len(line) == 0:
    pass  # {}

elif line == 'o hre':
    print('(c)2023 created by mirek')
    print('Dalsie dobrodruzstvo indiana jonesa tentokrat vytvorene v jazyku Python.')

elif line == 'prikazy':
    print('V hre je možné použiť tieto príkazy:')
    print('* o hre - zobrazí informácie o hre')
    print('* prikazy - zobrazí zoznam dostupných príkazov v hre')

else:
    print('Taký príkaz nepoznám.')

print('koniec')
