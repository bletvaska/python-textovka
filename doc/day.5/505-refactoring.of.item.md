# Úprava triedy `Item`

Pri používaní predmetov sme vytvorili dohodu, že predmet sa dá použiť len vtedy, ak má v zozname vlastností vlastnosť `USABLE`. Dopad tejto dohody znamená to, že predmet má zadefinovanú metódu `.use()`.

Samozrejme - táto dohoda je naivná, ale pre naše riešenie je dostatočná. Aby sme sa vyhli tomu, že programátor zavolá metódu `.use()` nad predmetom, ktorý túto metódu nemá zadefinovanú (buď nie je použiteľný alebo ešte nie je vytvorená), vyvoláme výnimku `NotImplementedError`. To zabezpečíme tak, že túto metódu vytvoríme už v rodičovskej triede a každý predmet, ktorý bude implementovať svoje vlastné použitie, tútu metódu prepíše (override) svojou vlastnostnou implementáciou.

Metóda `.use()` bude mať jeden parameter, ktorým bude kontext hry (objekt typu `GameContext`). Tu treba dať pozor na vznik cyklického importu.

```python
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from game_context import GameContext


class Item(BaseModel):
    name: str
    description: str
    features: list[int] = []

    def use(self, context: 'GameContext'):
        raise NotImplementedError('Usage of item was not yet implemented.')

    def examine(self, context: 'GameContext'):
        raise NotImplementedError('Examination of item was not yet implemented.')
```
