from dataclasses import dataclass

from models import Context


@dataclass(frozen=True)
class About:
    name: str = "o hre"
    description: str = "zobrazí informácie o hre"

    def exec(self, context: Context, name: str):
        print(
            "Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou."
        )
        print("Túto hru spáchal v 2022 (c) mirek.")
