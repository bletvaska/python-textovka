def go_west(context):
    """
    Move to the room on the west.

    If there is an exit to the west from the current room, then current room will change to the room on the west. \
    If the room on the west doesn't exist, then room will not change. And the message will be printed out. On the screen \
     of course.
    :param context: reference to the game context
    :return: nothing
    """

    if 'west' in context.current_room._exits:
        context.current_room = context.current_room._exits['west']
        print(context.current_room)
    else:
        print('tam sa neda ist.')


def go_east(context):
    if 'east' in context.current_room._exits:
        context.current_room = context.current_room._exits['east']
        print(context.current_room)
    else:
        print('tam sa neda ist.')


def go_down(context):
    if 'down' in context.current_room._exits:
        context.current_room = context.current_room._exits['down']
        print(context.current_room)
    else:
        print('tam sa neda ist.')


def commands():
    print('Zoznam prikazov:')
    print('\tkoniec - ukonci tuto mocnu hru')
    print('\to autorovi - zobrazi info o autorovi')
    print('\tprikazy - zobrazi zoznam prikazov')


def about():
    print(
        'ta to je iny sumny mladenec toten autor. by si ho mohol podporit mocnym fsimnym na ucet SK1234567890. ale fakt mocnym.')
    print('to je asi fsetko, co by si o nom mohol vediet. verejne.')


def quit(context):
    print('dakujem ze si si zahral, ale by si si to mohol aj rozmysliet, ci chces skoncit tuto mocnu hru.')
    context.game_state = 'QUIT'
