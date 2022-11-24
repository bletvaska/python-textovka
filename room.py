from dataclasses import dataclass, field


@dataclass
class Room:
    name: str
    description: str
    items: list = field(default_factory=list)
    exits: dict = field(default_factory=dict)

    def show(self):
        """
        Nachádzaš sa v miestnosti {self.name}
        {self.description}
        Z tejto miestnosti nevedú žiadne východy.
        """

        """
        Nachádzaš sa v miestnosti {name}
        {description}
        Možné východy z miestnosti::
        * sever
        """

        pass
