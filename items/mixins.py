from context import Context


class UsableMixin:
    def use(self, context: Context):
        raise NotImplementedError('Usage of this item is not yet implemented.')