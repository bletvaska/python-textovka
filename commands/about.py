def _exec(context: dict, param: str):
    print('(c)2021 created by mirek')
    print('Ďalšie veľké dobrodružstvo Indiana Jonesa. Tentokrát zápasí s jazykom Python v tmavej miestnosti.')


cmd = {
    'name': 'o hre',
    'description': 'zobrazí informácie o hre',
    'aliases': ('about', 'info', '?'),
    'exec': _exec,
}
