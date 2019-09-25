def show_room(room):
    # show description
    print(room['description'])

    # show exits
    if len(room['exits']) > 0:
        print('Možné východy:')
        for exit in room['exits']:
            print(f"    {exit}")
    else:
        print('Z miestnosti nevedú žiadne východy.')

    # show items
    if len(room['items']) > 0:
        print('Vidíš:')
        for item in room['items']:
            print(f'     {item["name"]}')
    else:
        print('Nevidíš nič zvláštne.')


def show_inventory(backpack):
    if len(backpack) > 0:
        print('V batohu máš:')
        for item in backpack:
            print(f'     {item["name"]}')
    else:
        print('Batoh je prázdny.')