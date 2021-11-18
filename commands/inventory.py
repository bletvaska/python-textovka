def _exec(context: dict, param: str):
    if context['backpack']['items'] == []:
        print("Batoh je prázdny.")
    else:
        print("V batohu máš:")
        for item in context['backpack']['items']:
            print(f"   * {item['name']}")


cmd = {
    'name': 'inventar',
    'description': 'zobrazí obsah batohu',
    'aliases': ("i", "inventory", 'batoh'),
    'exec': _exec,
}
