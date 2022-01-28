from items import bucket, canister, door, matches


world = [
    {
        "description": "Nachádzaš sa v tmavej miestnosti, v ktorej rozhodne chýbajú okná. "
        "Je tu značne šero a vlhko. Chladné kamenné steny dávajú tušiť, že "
        "sa nachádzaš v podzemí.",
        "items": [
            canister,
            door,
            matches,
            bucket,
        ],
        "exits": {"north": None, "south": None, "east": None, "west": None},
        "name": "dungeon",
    },
    {
        "name": "garden",
        "description": "Neudržiavaná plocha, ktorá sa pred pár rokmi určite nazývala záhradkou. Tuto boli asi zemiaky a tuto hľa asi aj krumpeľe.",
        "items": [],
        "exits": {"north": "heaven", "south": "hell", "east": None, "west": "dungeon"},
    },
    {
        "name": "heaven",
        "description": "Dvojnásobné RAMky. Dvojnásobné platy. Smiech a džavot naokolo. No to musí byť Dojč... Nebo.",
        "items": [],
        "exits": {"north": None, "south": "garden", "east": None, "west": None},
    },
    {
        "name": "hell",
        "description": "Ta teplo tu je. Začínam sa topiť vo vlastnej šťave. Ale aj v cudzej. Plač a škrípanie zubov. Python vo verzii 2.7.",
        "items": [],
        "exits": {"north": None, "south": None, "east": None, "west": None},
    },
]


# world = {
#     'dungeon':     {
#         "description": "Nachádzaš sa v tmavej miestnosti, v ktorej rozhodne chýbajú okná. "
#         "Je tu značne šero a vlhko. Chladné kamenné steny dávajú tušiť, že "
#         "sa nachádzaš v podzemí.",
#         "items": [
#             canister,
#             door,
#             matches,
#             bucket,
#         ],
#         "exits": {"north": None, "south": None, "east": None, "west": None},
#         "name": "dungeon",
#     },
#     'garden':     {
#         "name": "garden",
#         "description": "Neudržiavaná plocha, ktorá sa pred pár rokmi určite nazývala záhradkou. Tuto boli asi zemiaky a tuto hľa asi aj krumpeľe.",
#         "items": [],
#         "exits": {"north": None, "south": None, "east": None, "west": "dungeon"},
#     },
# }
