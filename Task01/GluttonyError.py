from Task01.AbstractError import AbstractError


class GluttonyError(AbstractError):

    def __str__(self):
        return "Вы переели..."
