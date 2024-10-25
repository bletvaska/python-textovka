# Game Context

Aktuálne vkladáme pri volaní metódy `.exec()` nad jednotlivými príkazmi hry dva parametre: batoh a zoznam príkazov. Ak sa však nad tým zamyslíme, budeme mať tých parametrov stále viac a viac. A hádam nechceme skončiť ako knižnica _Pandas_, ktorá má funkcie s desiatkami parametrov... :-)

Miesto toho zabalíme všetky tieto parametre do jedného objektu, ktorý nazveme **herný kontext** alebo **kontext hry**. Bude sa jednať o triedu, ktorá bude mať len vlastnosti a žiadne metódy. Tieto vlastnosti budú potrebné na to, aby sme vedeli v každom momente hry povedať, čo sa deje a mali sme k dispozícii všetko potrebné.
