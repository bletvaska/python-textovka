from game_context import GameContext


class Usable(object):
    def use(self, context: GameContext):
        raise NotImplementedError(f'Method use() was not implemented in item {self._name}.')