from .features import USABLE, MOVABLE

name = 'kanister'

description = '10 litrový kanister plný kvalitného slovnafťáckeho vysokooktánového 95% benzínu.'

features = [
    USABLE,
    MOVABLE
]

def use():
    # 1. preconditions
    # * dvere su v miestnosti
    #   - Zohol si sa, vzal si plny kanister do ruky a zacal si posilovat. Ved predsa plati, ze v zdravom tele zdravy duch.

    # 2. action
    # * polejeme dvere
    #   - aktualizujeme dvere - description, name
    # * aktualizujeme kanister
    #   - kanister uz nebude USABLE
    #   - aktualizujeme description

    # 3. render
    # Odsroboval si vrchnak kanistru a cely jeho obsah si vylial na velke masivne dvere. Doteraz tu bol taky pokoj a klud, ale odteraz sa vzduchom rozplyva vona 95% kvalitneho vysokooktanoveho benzinu z ruska.