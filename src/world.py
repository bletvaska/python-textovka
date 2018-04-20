world = {}

world["garaz"] = {
    "name": "garaz",
    "description": "nachadzas sa v temnom priestore garazovom v budove globallogic. nie si v kurfri, aj ked to "
                   "tak vyzera, pretoze jedina lampa, ktora sa tu nachadza, je tiez pokazena.",
    "exits": [],
    "items": [
        {
            "name": "pneumatika",
            "description": "Čierna pneumatika značky Barum deravá len na dvoch miestach.",
            "features": []
        },
        {
            "name": "hummer",
            "description": "Štvorkolesový mocný hummer. Tiež pokazený.",
            "features": []
        },
        {
            "name": "kluc",
            "description": "Standardna FABka.",
            "features": ["movable", "usable"]
        }
    ]
}

world["vytah"] = {
    "name": "vytah",
    "description": "magicka vytahova kabinka ta vita s usmevom. dolezite upozornenie: vytah je pokazeny.",
    "exits": ["schodisko"],
    "items": [
        {
            'name': 'ovladac',
            'description': 'Ovládač výťahu s množstvom gombíkov reprezentujúcich jednotlivé poschodia.',
            'features': ['usable']
        },
        {
            'name': 'ochrankar',
            'description': 'Zavalitý chlapík ukrajinského typu. Jedným slovom vyhadzovač. Z jeho očí nesrší nič dobré.',
            'features': [],
            'has cafe': False
        }
    ]
}

world["schodisko"] = {
    "name": "schodisko",
    "description": "si na zaciatku schodiska veduceho do vysin tejto vysokej budovy. uz ti zostava len 23567643245678 "
                   "schodov, aby si sa dostal celkom hore.",
    "exits": ["vytah", "garaz"],
    "items": [
        {
            "name": "kladivo",
            "description": "Veľké obojručné kladivo pripomínajúce to, ktoré nosil Gimli. Týmto sa rezne určite nevyklepávajú.",
            "features": ["movable"]
        },
        {
            "name": "kavomat",
            "description": "Mocný prístroj na tvorbu zázračného tmavého moku s neznámym obsahom, ktorý zachránil život nejednému Pythonistovi.",
            "features": ['usable']
        }
    ]
}
