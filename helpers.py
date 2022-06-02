def intro():
    """
    The game intro banner.
    """
    print(' ___           _ _                         _')
    print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___')
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(' | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\')
    print('|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/')

    print('                         and his Great Escape')


def outro():
    """
    The game outro banner.
    """
    print('Dobru chut.')


def get_item_by_name(name, items):
    for item in items:
        if name == item.name:
            return item

    # return None
