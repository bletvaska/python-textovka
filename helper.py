def find_item(name, context):
    items = context['room']['items'] + context['inventory']
    for item in items:
        if item['name'] == name:
            return item


def show_room(room):
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if len(room['items']) == 0:
        print('V miestnosti sa nenachadzaju ziadne predmety.')
    else:
        print(f'V miestnosti si nasiel tieto predmety:')
        for item in room['items']:
            print(f'\t* {item["name"].lower()}')

    if len(room['exits']) == 0:
        print('Z miestnosti neexistujú žiadne východy.')
    else:
        print(f'Východy z miestnosti: {room["exits"]}.')