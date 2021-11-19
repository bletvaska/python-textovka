from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    name = context['room']['exits']['west']
    if name is None:
        print('Tam sa nedá ísť.')
    else:
        # save to history
        context['history'].append(f'{cmd["name"]}')

        # go west
        print('Kráčaš na západ.')
        room = get_room_by_name(context['world'], name)
        context['room'] = room
        show_room(room)


cmd = {
    'name': "zapad",
    'description': 'presunie sa do miestnosti na západ, ak sa tým smerom da ísť.',
    'aliases': ("west",),
    'exec': _exec,
}
