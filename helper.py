def find_item(name: str, context: dict) -> dict:
    """
    Finds item in current room and inventory

    :param name: the name of the item to find
    :param context: context object (with room and inventory)
    :return: reference to the item dictionary if found, `None` otherwise
    """
    room_name = context['room']
    room = context['world'][room_name]
    items = room['items'] + context['inventory']
    for item in items:
        if item['name'] == name:
            return item


def show_room(room):
    """
    Shows the content of the room

    :param room: the room to show
    """
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