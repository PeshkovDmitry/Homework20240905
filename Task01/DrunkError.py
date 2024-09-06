from Task01.AbstractError import AbstractError


class DrunkError(AbstractError):

    def __str__(self):
        return "Вы выпили лишнего..."
