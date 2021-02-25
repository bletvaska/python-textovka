def show_room(room):
    # nazov a opis miestnosti
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(room['description'])

    # vypis vychodov z miestnosti
    if room['exits']['east'] == None and room['exits']['west'] == None and room['exits']['south'] == None and room['exits']['north'] == None:
        print('Z miestnosti neexistujú žiadne východy.')
    else:
        print('Možné východy z miestnosti:')
        if room['exits']['east'] != None:
            print('  vychod')
        if room['exits']['west'] != None:
            print('  zapad')
        if room['exits']['south'] != None:
            print('  juh')
        if room['exits']['north'] != None:
            print('  sever')

    # vypis predmetov v miestnosti
    if len(room['items']) == 0:
        print('Nevidíš tu nič zaujímavé.')
    else:
        print('Vidíš:')
        for item in room['items']:
            print(f'  {item["name"]}')
