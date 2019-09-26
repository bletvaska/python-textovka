from game_context import GameContext


class MovableMixin(object):
    pass


class UsableMixin(object):
    def exec(self, context: GameContext):
        raise NotImplementedError()
