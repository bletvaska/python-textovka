def go_west(context):
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
