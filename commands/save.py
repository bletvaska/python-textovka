from dataclasses import dataclass
import json

from models import Context


@dataclass
class Save:
    name: str = "uloz"
    description: str = "uloží stav hry do súboru"

    def exec(self, context: Context, name: str):
        # if no item was given, then quit
        if len(name) == 0:
            print("Neviem, do akého súboru chceš uložiť svoju pozíciu.")
            return

        # save
        try:
            with open(name, "w") as file:
                json.dump(context.history, file, indent=4)

                print(f"Aktuálna pozícia bola úspešne uložená do súboru {name}")

        except PermissionError:
            print("Pri ukladaní súboru došlo k chybe: chyba prístupu.")

        except FileNotFoundError:
            print(
                "Pri ukladaní súboru došlo k chybe: súbor alebo priečinok nebol nájdený."
            )

        except Exception:
            print("Pri ukladaní súboru došlo k chybe.")
