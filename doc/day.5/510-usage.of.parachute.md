# Použitie padáku

Indiana Jones sa zachráni tým, že po vyskočení z lietadla použije padák. To znamená, že v implementácii predmetu `padak`
vytvorte metódu `.use()`, v ktorej implementujete použitie tohto predmetu.

Použitie padáku znamená:

1. overiť, či sa hráč nachádza v miestnosti `voľný pád` (ak nie, vráťte hodnotu `False`)
2. ak sa hráč v miestnosti nachádza, tak:

   * Indy pristane (presunie sa) do miestnosti s názvom `púšť`, a
   * vypíšte na obrazovku správu
     ```
     Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...
     ```
3. po použití sa padák stane automaticky nepoužiteľný


## Použitie padáku

```python
class Parachute(Item):
   name: str = 'padak'
   description: str = 'Made in USA 1939'
   features: list[int] = [MOVABLE, USABLE]

   def use(self, context) -> bool:
       # if not in correct room
       if context.current_room.name != 'voľný pád':
           return False

       # action
       room = get_room_by_name('púšť', context.world)
       context.current_room = room

       # render
       print('[bold green]Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...[/bold green]')
       room.show()
       return True
```
