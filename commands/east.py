from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    name = context['room']['exits']['east']
    if name is None:
        print('Tam sa nedá ísť.')
    else:
        # save to history
        context['history'].append(f'{cmd["name"]}')

        # go east
        print('Kráčaš na východ.')
        room = get_room_by_name(context['world'], name)
        context['room'] = room
        show_room(room)


cmd = {
    'name': "vychod",
    'description': 'presunie sa do miestnosti na východ, ak sa tým smerom da ísť.',
    'aliases': ("east",),
    'exec': _exec,
}
