def _exec(context: dict, param: str):
    print('Zoznam príkazov v hre:')
    for cmd in context['commands']:
        print(f'* {cmd["name"]} - {cmd["description"]}')


cmd = {
    'name': 'prikazy',
    'description': 'zobrazí príkazy, ktoré sa dajú použiť v hre',
    'aliases': ('commands', 'help', 'pomoc',),
    'exec': _exec
}
