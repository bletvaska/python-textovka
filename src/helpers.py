import states

def intro():
    """
    Shows the intro screen of the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('                   and his Great Python Adventure')
    print()


def outro():
    """
    Shows the outro screen of the game.
    """
    print('Ďakujem, že si si zahral túto mimoriadne fantastickú hru. Podpor mladého autora prevedním vhodnej čiastky na jeho účet. Díky.')


def ask_yes_no(question):
    choice = input(f'{question} (a/n) ').strip().lower()

    while choice not in ['ano', 'a', 'yes', 'y', 'nie', 'n', 'no', 'áno']:
        choice = input(f'Nesprávny vstup. {question} Zadaj prosím a/n ').strip().lower()

    return choice in ['a', 'ano', 'áno', 'yes', 'y']
