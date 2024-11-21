# Aktuálna miestnosť v hre

Počas hrania hry bude potrebné vždy vedieť, v ktorej miestnosti sa hráč nachádza. Preto rozšírime triedu
`GameContext` o novú členskú premennú s názvom `current_room`, ktorá bude typu `Room`. Predvolená hodnota nech je
`None`.

```python
class GameContext(BaseModel):
    backpack: list = []
    commands: list[Command] = []
    game_state: str = PLAYING
    current_room: Room = None
```
