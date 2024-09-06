from Task01.AbstractError import AbstractError


class DepressionError(AbstractError):

    def __str__(self):
        return "Вы в депрессии..."
