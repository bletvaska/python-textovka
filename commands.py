from pydantic import BaseModel


class Command(BaseModel):
    name: str
    description: str

    def exec(self):
        print('>>> chyba implementacia metody exec')


class About(Command):
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self):
        print('Túto mocnú hru spáchal mocný programátor mirek')
        print('(c)2023 by mirek')


class Commands(Command):
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'
