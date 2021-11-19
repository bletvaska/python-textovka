from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    name = context['room']['exits']['north']
    if name is None:
        print('Tam sa nedá ísť.')
    else:
        print('Kráčaš na sever.')
        room = get_room_by_name(context['world'], name)
        context['room'] = room
        show_room(room)


cmd = {
    'name': "sever",
    'description': 'presunie sa do miestnosti na sever, ak sa tým smerom da ísť.',
    'aliases': ("north",),
    'exec': _exec,
}
