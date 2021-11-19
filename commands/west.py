from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    name = context['room']['exits']['west']
    if name == None:
        print('Tam sa nedá ísť.')
    else:
        print('Kráčaš na západ.')
        context['room'] = get_room_by_name(context['world'], name)
        show_room(context['room'])


cmd = {
    'name': "zapad",
    'description': 'presunie sa do miestnosti na západ, ak sa tým smerom da ísť.',
    'aliases': ("west",),
    'exec': _exec,
}
