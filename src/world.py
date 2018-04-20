"""
The definition of the world is located here.

World is simple dictionary, where every location (or as we defined in the game - the room) is defined. Every room has:
* name
* description
* available exits
* list of items located in the room
"""

world = {
    "chodba": {
        "description": "nachadzas sa na chodbe. Tmava, seda, zo stropu kvapka voda. I have a bad feeling about this "
                       "place... ",
        "name": "chodba",
        "exits": ["kuchynka", "l4"],
        "items": [

        ]
    },

    "kuchynka": {
        "description": "fajna kuchynka s nabytkom z ikei. skoda, ze tu nesvieti svetlo, aby si mohol obdivovat krasy "
                       "novych spotrebicov.",
        "name": "kuchynka",
        "exits": ["chodba"],
        "items": [
            {
                "name": "spekacky",
                "description": "Fajne, sumne spekacky, ktore tvojej diete urcite neuskodia.",
                "features": ["movable", "usable"]
            },
            {
                "name": "smalec",
                "description": "Husty biely smalec, ktorym namazes kazdy krajec chleba.",
                "features": ["movable"]
            }
            ,
            {
                "name": "kladivo",
                "description": "Velke obojrucne kladivo, ktore rozhodne nie je vhodne na vyklepavanie reznov.",
                "features": ["movable"]

            },
            {
                "name": "kavomat",
                "description": "Veľký pekelný kávomat podávajúci zdarma zázračný mok, ktorý zachránil život nejednému Pythonistovi. Alebo aspoň zahrial.",
                "features": ["usable"]
            }
        ]
    },

    "l4": {
        "description": "nachadzas sa v skoliacej miestnosti L4. peta sa tu vysmieva (asi skolitelovi). vonku vidiet "
                       "zeriav. ako cosi vezie na ramene. ",
        "name": "l4",
        "exits": [],
        "items": [
            {
                "name": "pocitac",
                "description": "Maly prenosny pocitac nevsednych rozmerov. Znacka: aj s podvozkom.",
                "features": ['usable']
            },
            {
                "name": "kluc",
                "description": "Fajný hrdzavý klúčik značky FAB.",
                "features": ['movable', 'usable']
            },
            {
                "name": "instruktor",
                "description": "Vysoký, sympatický a najobľúbenejší, a najskromnejší inštruktor teráristického kurzu o Pythónoch. Zasa je nervózny.",
                "features": [],
                "happy": False
            }
        ]
    }
}
