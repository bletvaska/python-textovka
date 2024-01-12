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

## Použitie padáku

```python
class Parachute(Item):
   name = 'padak'
   description = 'Made in USA 1939'
   features = [MOVABLE, USABLE]

   def use(self, context):
      # if not in correct room
      if context.current_room.name != 'voľný pád':
         print('Podľa teba som zrejme blbec, ale naozaj nechápem, k čomu by to v súčasnej dobe bolo dobré.')
         return

      # action
      room = get_room_by_name('púšť', context.world)
      context.current_room = room

      # render
      print('[bold green]Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...[/bold green]')
      room.show()
```
