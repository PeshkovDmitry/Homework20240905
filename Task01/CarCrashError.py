from Task01.AbstractError import AbstractError


class CarCrushError(AbstractError):

    def __str__(self):
        return "Вы попали в аварию..."
