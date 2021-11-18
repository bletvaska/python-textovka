import states


def _exec(context: dict, param: str):
    context['state'] = states.QUIT


cmd = {
    'name': 'koniec',
    'description': 'ukončí rozohratú hru',
    'aliases': ('quit', 'bye', 'q', 'exit',),
    'exec': _exec,
}
