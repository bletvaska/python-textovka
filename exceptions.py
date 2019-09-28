class GameException(BaseException):
    pass


class FullBackpackException(GameException):
    pass


class ItemNotFoundException(GameException):
    pass
