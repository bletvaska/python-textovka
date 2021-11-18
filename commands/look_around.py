from helpers import show_room


def _exec(context: dict, param: str):
    show_room(context['room'])


cmd = {
    'name': "rozhliadni sa",
    'description': 'vypíše opis miestnosti, v ktorej sa hráč práve nachádza',
    'aliases': ("look around", "kukaj het"),
    'exec': _exec,
}
