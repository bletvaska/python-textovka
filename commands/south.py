from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    name = context['room']['exits']['south']
    if name is None:
        print('Tam sa nedá ísť.')
    else:
        # save to history
        context['history'].append(f'{cmd["name"]} {param}')

        # go south
        print('Kráčaš na juh.')
        room = get_room_by_name(context['world'], name)
        context['room'] = room
        show_room(room)


cmd = {
    'name': "juh",
    'description': 'presunie sa do miestnosti na juh, ak sa tým smerom da ísť.',
    'aliases': ("south",),
    'exec': _exec,
}
