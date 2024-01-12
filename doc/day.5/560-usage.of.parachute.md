# Použitie padáku



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
