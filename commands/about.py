from dataclasses import dataclass, field


@dataclass
class About:
    name: str = 'o hre'
    description: str = 'vypíše info o hre'
    # aliases: list[str] = field(default_factory=['o hre', 'about', 'info', '?'])

    def exec(self):
        pass
