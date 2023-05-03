print("Indiana Jones and his Greatest Python Adventure")
line = None

while line != 'koniec':
    line = input('> ').lower().lstrip().rstrip()

    if line == 'o hre':
        print('Túto mocnú hru spáchal mocný programátor mirek')
        print('(c)2023 by mirek')

    elif line == 'pre evku':
        print('toto je vyrobene vylucne pre evku.')

    elif line == 'prikazy':
        print('Zoznam dostupnych prikazov v hre:')
        print('* o hre - zobrazi informacie o hre')
        print('* prikazy - zobrazi zoznam dostupnych prikazov')

    elif line == 'koniec':
        print('Díky, že si si zahral túto mocnú hru.')

    else:
        print('Taký príkaz nepoznám.')

print('koniec')
